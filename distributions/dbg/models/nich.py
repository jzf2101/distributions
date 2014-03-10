"""
A conjugate model on normally-distributied univariate data in which the
prior on the mean is normally distributed, and the prior on the variance
is Inverse-Chi-Square distributed.

The equations used here are from \cite{murphy2007conjugate}.
Murphy, K. "Conjugate Bayesian analysis of the Gaussian distribution" (2007)
Equation numbers referenced below are from this paper.
"""

from distributions.dbg.special import sqrt, log, pi, gammaln
from distributions.dbg.random import sample_chi2, sample_normal
from distributions.mixins import ComponentModel, Serializable


# FIXME how does this relate to distributions.dbg.random.score_student_t
def score_student_t(x, nu, mu, sigmasq):
    """
    \cite{murphy2007conjugate}, Eq. 304
    """
    score = gammaln(.5 * (nu + 1.)) - gammaln(.5 * nu)
    score -= .5 * log(nu * pi * sigmasq)
    xt = (x - mu)
    s = xt * xt / sigmasq
    score += -(.5 * (nu + 1.)) * log(1. + s / nu)
    return score


class NormalInverseChiSq(ComponentModel, Serializable):
    def __init__(self):
        self.mu = None
        self.kappa = None
        self.sigmasq = None
        self.nu = None

    def load(self, raw):
        self.mu = float(raw['mu'])
        self.kappa = float(raw['kappa'])
        self.sigmasq = float(raw['sigmasq'])
        self.nu = float(raw['nu'])

    def dump(self):
        return vars(self)

    #-------------------------------------------------------------------------
    # Datatypes

    Value = float

    class Group(object):
        def __init__(self):
            self.count = None
            self.sampmean = None
            self.allsampvar = None  # = count * variance

        def load(self, raw):
            self.count = int(raw['count'])
            self.sampmean = float(raw['sampmean'])
            self.allsampvar = float(raw['allsampvar'])

        def dump(self):
            return vars(self)

    #-------------------------------------------------------------------------
    # Mutation

    def group_init(self, group):
        group.count = 0
        group.sampmean = 0.
        group.allsampvar = 0.

    def group_add_value(self, group, value):
        group.count += 1
        delta = value - group.sampmean
        group.sampmean += delta / group.count
        group.allsampvar += delta * (value - group.sampmean)

    def group_remove_value(self, group, value):
        total = group.sampmean * group.count
        delta = value - group.sampmean
        group.count -= 1
        if group.count == 0:
            group.sampmean = 0.
        else:
            group.sampmean = (total - value) / group.count
        if group.count <= 1:
            group.allsampvar = 0.
        else:
            group.allsampvar -= delta * (value - group.sampmean)

    def group_merge(self, destin, source):
        count = destin.count + source.count
        delta = source.sampmean - destin.sampmean
        source_part = float(source.count) / count
        cross_part = destin.count * source_part
        destin.count = count
        destin.sampmean += source_part * delta
        destin.allsampvar += source.allsampvar + cross_part * delta * delta

    def plus_group(self, group):
        """
        \cite{murphy2007conjugate}, Eqs.141-144
        """
        total = group.sampmean * group.count
        mu_1 = self.mu - group.sampmean
        kappa_n = self.kappa + group.count
        mu_n = (self.kappa * self.mu + total) / kappa_n
        nu_n = self.nu + group.count
        sigmasq_n = 1. / nu_n * (
            self.nu * self.sigmasq
            + group.allsampvar
            + (group.count * self.kappa * mu_1 * mu_1) / kappa_n)

        post = self.__class__()
        post.mu = mu_n
        post.kappa = kappa_n
        post.nu = nu_n
        post.sigmasq = sigmasq_n
        return post

    #-------------------------------------------------------------------------
    # Sampling

    def sampler_create(self, group=None):
        """
        Draw samples from the marginal posteriors of mu and sigmasq

        \cite{murphy2007conjugate}, Eqs. 156 & 167
        """
        z = self if group is None else self.plus_group(group)
        # Sample from the inverse-chi^2 using the transform from the chi^2
        sigmasq_star = z.nu * z.sigmasq / sample_chi2(z.nu)
        mu_star = sample_normal(z.mu, sqrt(sigmasq_star / z.kappa))
        return (mu_star, sigmasq_star)

    def sampler_eval(self, sampler):
        mu, sigmasq = sampler
        return sample_normal(mu, sqrt(sigmasq))

    def sample_value(self, group):
        sampler = self.sampler_create(group)
        return self.sampler_eval(sampler)

    def sample_group(self, size):
        sampler = self.sampler_create()
        return [self.sampler_eval(sampler) for _ in xrange(size)]

    #-------------------------------------------------------------------------
    # Scoring

    def score_value(self, group, value):
        """
        \cite{murphy2007conjugate}, Eq. 176
        """
        z = self.plus_group(group)
        return score_student_t(
            value,
            z.nu,
            z.mu,
            ((1 + z.kappa) * z.sigmasq) / z.kappa)

    def score_group(self, group):
        """
        \cite{murphy2007conjugate}, Eq. 171
        """
        z = self.plus_group(group)
        return gammaln(z.nu / 2.) - gammaln(self.nu / 2.) \
            + 0.5 * log(self.kappa / z.kappa) \
            + (0.5 * self.nu) * log(self.nu * self.sigmasq) \
            - (0.5 * z.nu) * log(z.nu * z.sigmasq) \
            - group.count / 2. * 1.1447298858493991

    #-------------------------------------------------------------------------
    # Examples

    EXAMPLES = [
        {
            'model': {'mu': 0., 'kappa': 1., 'sigmasq': 1., 'nu': 1.},
            'values': [-4.0, -2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 4.0],
        },
    ]


Model = NormalInverseChiSq
