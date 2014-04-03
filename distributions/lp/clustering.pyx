# Copyright (c) 2014, Salesforce.com, Inc.  All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# - Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# - Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# - Neither the name of Salesforce.com nor the names of its contributors
#   may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
# OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
# TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from libcpp.vector cimport vector
from libcpp.utility cimport pair
cimport numpy
numpy.import_array()
from cython.operator cimport dereference as deref, preincrement as inc
from distributions.rng_cc cimport rng_t
from distributions.global_rng cimport get_rng
from distributions.lp.vector cimport VectorFloat, vector_float_to_ndarray


cdef extern from 'distributions/clustering.hpp':

    cppclass Assignments "distributions::Clustering<int>::Assignments":
        Assignments() nogil except +
        cppclass iterator:
            pair[int, int] & operator*() nogil
            iterator operator++() nogil
            bint operator!=(iterator) nogil
        int & operator[](int) nogil
        iterator begin() nogil
        iterator end() nogil

    cdef vector[int] count_assignments_cc \
            "distributions::Clustering<int>::count_assignments" \
            (Assignments & assignments) nogil except +

    cppclass PitmanYor_cc "distributions::Clustering<int>::PitmanYor":
        float alpha
        float d
        vector[int] sample_assignments(int size, rng_t & rng) nogil except +
        cppclass Mixture:
            vector[int] counts
            int sample_size
            VectorFloat shifted_scores
        float score_counts(vector[int] & counts) nogil except +
        float score_add_value (
                int group_size,
                int group_count,
                int sample_size) nogil except +
        float score_remove_value (
                int group_size,
                int group_count,
                int sample_size) nogil except +
        void mixture_init (Mixture &) nogil except +
        void mixture_add_group (Mixture &) nogil except +
        void mixture_remove_group (Mixture &, size_t) nogil except +
        void mixture_add_value (Mixture &, size_t) nogil except +
        void mixture_remove_value (Mixture &, size_t) nogil except +
        void mixture_score (Mixture &, VectorFloat &) nogil except +

    cppclass LowEntropy_cc "distributions::Clustering<int>::LowEntropy":
        int dataset_size
        vector[int] sample_assignments(int size, rng_t & rng) nogil except +
        float score_counts(vector[int] & counts) nogil except +
        float score_add_value (
                int group_size,
                int group_count,
                int sample_size) nogil except +
        float score_remove_value (
                int group_size,
                int group_count,
                int sample_size) nogil except +


cpdef list count_assignments(dict assignments):
    cdef Assignments assignments_cc
    cdef int value_id
    cdef int group_id
    for value_id, group_id in assignments.iteritems():
        assignments_cc[value_id] = group_id
    cdef list counts = count_assignments_cc(assignments_cc)
    return counts


cdef dict dump_assignments(Assignments & assignments):
    cdef dict raw = {}
    cdef Assignments.iterator i = assignments.begin()
    while i != assignments.end():
        assignments[deref(i).first] = deref(i).second
        inc(i)
    return raw


cdef class PitmanYorMixture:
    cdef PitmanYor_cc.Mixture * ptr
    def __cinit__(self):
        self.ptr = new PitmanYor_cc.Mixture()
    def __dealloc__(self):
        del self.ptr

    def __len__(self):
        return self.ptr.counts.size()

    def append(self, int count):
        self.ptr.counts.push_back(count)

    def clear(self):
        self.ptr.counts.clear()


cdef class PitmanYor_cy:
    cdef PitmanYor_cc * ptr
    def __cinit__(self):
        self.ptr = new PitmanYor_cc()
    def __dealloc__(self):
        del self.ptr

    def __init__(self, **kwargs):
        if kwargs:
            self.load(kwargs)
        else:
            self.ptr.alpha = 1.0
            self.ptr.d = 0.0

    def load(self, dict raw):
        cdef float alpha = raw['alpha']
        cdef float d = raw['d']
        assert 0 < alpha
        assert 0 <= d and d < 1
        self.ptr.alpha = alpha
        self.ptr.d = d

    def dump(self):
        return {
            'alpha': self.alpha,
            'd': self.d,
        }

    def sample_assignments(self, int size):
        cdef list assignments = self.ptr.sample_assignments(size, get_rng()[0])
        return assignments

    def score_counts(self, list counts):
        cdef vector[int] counts_cc = counts
        cdef float score = self.ptr.score_counts(counts_cc)
        return score

    def score_add_value(
            self,
            int group_size,
            int group_count,
            int sample_size):
        return self.ptr.score_add_value(group_size, group_count, sample_size)

    def score_remove_value(
            self,
            int group_size,
            int group_count,
            int sample_size):
        return self.ptr.score_remove_value(
            group_size,
            group_count,
            sample_size)

    #-------------------------------------------------------------------------
    # Mixture

    def mixture_init(self, PitmanYorMixture mixture):
        self.ptr.mixture_init(mixture.ptr[0])

    def mixture_add_group(self, PitmanYorMixture mixture):
        self.ptr.mixture_add_group(mixture.ptr[0])

    def mixture_remove_group(self, PitmanYorMixture mixture, int groupid):
        self.ptr.mixture_remove_group(mixture.ptr[0], groupid)

    def mixture_add_value(self, PitmanYorMixture mixture, int groupid):
        self.ptr.mixture_add_value(mixture.ptr[0], groupid)

    def mixture_remove_value(self, PitmanYorMixture mixture, int groupid):
        self.ptr.mixture_remove_value(mixture.ptr[0], groupid)

    def mixture_score(
            self,
            PitmanYorMixture mixture,
            numpy.ndarray[numpy.float32_t, ndim=1] scores):
        cdef VectorFloat scores_cc
        scores_cc.resize(len(mixture))
        self.ptr.mixture_score(mixture.ptr[0], scores_cc)
        vector_float_to_ndarray(scores_cc, scores)


    #-------------------------------------------------------------------------
    # Examples

    EXAMPLES = [
        {'alpha': 1., 'd': 0.},
        {'alpha': 1., 'd': 0.1},
        {'alpha': 1., 'd': 0.9},
        {'alpha': 10., 'd': 0.1},
        {'alpha': 0.1, 'd': 0.1},
    ]


class PitmanYor(PitmanYor_cy):

    def load_protobuf(self, message):
        self.load({'alpha': message.alpha, 'd': message.d})

    def dump_protobuf(self, message):
        dumped = self.dump()
        message.Clear()
        message.alpha = dumped.alpha
        message.d = dumped.d

    #-------------------------------------------------------------------------
    # Datatypes

    Mixture = PitmanYorMixture


cdef class LowEntropy:
    cdef LowEntropy_cc * ptr
    def __cinit__(self):
        self.ptr = new LowEntropy_cc()
    def __dealloc__(self):
        del self.ptr

    def __init__(self, **kwargs):
        if kwargs:
            self.load(kwargs)
        else:
            self.ptr.dataset_size = 0

    def load(self, dict raw):
        cdef int dataset_size = raw['dataset_size']
        assert dataset_size >= 0
        self.ptr.dataset_size = dataset_size

    def dump(self):
        return {'dataset_size': self.ptr.dataset_size}

    def sample_assignments(self, int size):
        cdef list assignments = self.ptr.sample_assignments(size, get_rng()[0])
        return assignments

    def score_counts(self, list counts):
        cdef vector[int] counts_cc = counts
        cdef float score = self.ptr.score_counts(counts_cc)
        return score

    def score_add_value(
            self,
            int group_size,
            int group_count,
            int sample_size):
        return self.ptr.score_add_value(group_size, group_count, sample_size)

    def score_remove_value(
            self,
            int group_size,
            int group_count,
            int sample_size):
        return self.ptr.score_remove_value(
            group_size,
            group_count,
            sample_size)

    #-------------------------------------------------------------------------
    # Examples

    EXAMPLES = [
        {'dataset_size': 5},
        {'dataset_size': 10},
        {'dataset_size': 100},
        {'dataset_size': 1000},
    ]
