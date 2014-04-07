# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='distributions/io/schema.proto',
  package='protobuf.distributions',
  serialized_pb='\n\x1d\x64istributions/io/schema.proto\x12\x16protobuf.distributions\"\xdd\x01\n\nClustering\x12@\n\npitman_yor\x18\x01 \x01(\x0b\x32,.protobuf.distributions.Clustering.PitmanYor\x12\x42\n\x0blow_entropy\x18\x02 \x01(\x0b\x32-.protobuf.distributions.Clustering.LowEntropy\x1a%\n\tPitmanYor\x12\r\n\x05\x61lpha\x18\x01 \x02(\x02\x12\t\n\x01\x64\x18\x02 \x02(\x02\x1a\"\n\nLowEntropy\x12\x14\n\x0c\x64\x61taset_size\x18\x01 \x02(\x04\"S\n\rBetaBernoulli\x12\r\n\x05\x61lpha\x18\x01 \x02(\x02\x12\x0c\n\x04\x62\x65ta\x18\x02 \x02(\x02\x1a%\n\x05Group\x12\r\n\x05heads\x18\x01 \x02(\x04\x12\r\n\x05tails\x18\x02 \x02(\x04\"<\n\x11\x44irichletDiscrete\x12\x0e\n\x06\x61lphas\x18\x01 \x03(\x02\x1a\x17\n\x05Group\x12\x0e\n\x06\x63ounts\x18\x01 \x03(\x04\"n\n\x18\x44irichletProcessDiscrete\x12\r\n\x05gamma\x18\x01 \x02(\x02\x12\r\n\x05\x61lpha\x18\x02 \x02(\x02\x12\r\n\x05\x62\x65tas\x18\x03 \x03(\x02\x1a%\n\x05Group\x12\x0c\n\x04keys\x18\x01 \x03(\r\x12\x0e\n\x06values\x18\x02 \x03(\x04\"f\n\x0cGammaPoisson\x12\r\n\x05\x61lpha\x18\x01 \x02(\x02\x12\x10\n\x08inv_beta\x18\x02 \x02(\x02\x1a\x35\n\x05Group\x12\r\n\x05\x63ount\x18\x01 \x02(\x04\x12\x0b\n\x03sum\x18\x02 \x02(\x04\x12\x10\n\x08log_prod\x18\x03 \x02(\x02\"\x90\x01\n\x12NormalInverseChiSq\x12\n\n\x02mu\x18\x01 \x02(\x02\x12\r\n\x05kappa\x18\x02 \x02(\x02\x12\x0f\n\x07sigmasq\x18\x03 \x02(\x02\x12\n\n\x02nu\x18\x04 \x02(\x02\x1a\x42\n\x05Group\x12\r\n\x05\x63ount\x18\x01 \x02(\x04\x12\x0c\n\x04mean\x18\x02 \x02(\x02\x12\x1c\n\x14\x63ount_times_variance\x18\x03 \x02(\x02')




_CLUSTERING_PITMANYOR = descriptor.Descriptor(
  name='PitmanYor',
  full_name='protobuf.distributions.Clustering.PitmanYor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='alpha', full_name='protobuf.distributions.Clustering.PitmanYor.alpha', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='d', full_name='protobuf.distributions.Clustering.PitmanYor.d', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=206,
  serialized_end=243,
)

_CLUSTERING_LOWENTROPY = descriptor.Descriptor(
  name='LowEntropy',
  full_name='protobuf.distributions.Clustering.LowEntropy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='dataset_size', full_name='protobuf.distributions.Clustering.LowEntropy.dataset_size', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=245,
  serialized_end=279,
)

_CLUSTERING = descriptor.Descriptor(
  name='Clustering',
  full_name='protobuf.distributions.Clustering',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='pitman_yor', full_name='protobuf.distributions.Clustering.pitman_yor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='low_entropy', full_name='protobuf.distributions.Clustering.low_entropy', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CLUSTERING_PITMANYOR, _CLUSTERING_LOWENTROPY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=58,
  serialized_end=279,
)


_BETABERNOULLI_GROUP = descriptor.Descriptor(
  name='Group',
  full_name='protobuf.distributions.BetaBernoulli.Group',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='heads', full_name='protobuf.distributions.BetaBernoulli.Group.heads', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tails', full_name='protobuf.distributions.BetaBernoulli.Group.tails', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=327,
  serialized_end=364,
)

_BETABERNOULLI = descriptor.Descriptor(
  name='BetaBernoulli',
  full_name='protobuf.distributions.BetaBernoulli',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='alpha', full_name='protobuf.distributions.BetaBernoulli.alpha', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='beta', full_name='protobuf.distributions.BetaBernoulli.beta', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BETABERNOULLI_GROUP, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=281,
  serialized_end=364,
)


_DIRICHLETDISCRETE_GROUP = descriptor.Descriptor(
  name='Group',
  full_name='protobuf.distributions.DirichletDiscrete.Group',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='counts', full_name='protobuf.distributions.DirichletDiscrete.Group.counts', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=403,
  serialized_end=426,
)

_DIRICHLETDISCRETE = descriptor.Descriptor(
  name='DirichletDiscrete',
  full_name='protobuf.distributions.DirichletDiscrete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='alphas', full_name='protobuf.distributions.DirichletDiscrete.alphas', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DIRICHLETDISCRETE_GROUP, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=366,
  serialized_end=426,
)


_DIRICHLETPROCESSDISCRETE_GROUP = descriptor.Descriptor(
  name='Group',
  full_name='protobuf.distributions.DirichletProcessDiscrete.Group',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='keys', full_name='protobuf.distributions.DirichletProcessDiscrete.Group.keys', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='values', full_name='protobuf.distributions.DirichletProcessDiscrete.Group.values', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=501,
  serialized_end=538,
)

_DIRICHLETPROCESSDISCRETE = descriptor.Descriptor(
  name='DirichletProcessDiscrete',
  full_name='protobuf.distributions.DirichletProcessDiscrete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='gamma', full_name='protobuf.distributions.DirichletProcessDiscrete.gamma', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='alpha', full_name='protobuf.distributions.DirichletProcessDiscrete.alpha', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='betas', full_name='protobuf.distributions.DirichletProcessDiscrete.betas', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DIRICHLETPROCESSDISCRETE_GROUP, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=428,
  serialized_end=538,
)


_GAMMAPOISSON_GROUP = descriptor.Descriptor(
  name='Group',
  full_name='protobuf.distributions.GammaPoisson.Group',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='count', full_name='protobuf.distributions.GammaPoisson.Group.count', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sum', full_name='protobuf.distributions.GammaPoisson.Group.sum', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='log_prod', full_name='protobuf.distributions.GammaPoisson.Group.log_prod', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=589,
  serialized_end=642,
)

_GAMMAPOISSON = descriptor.Descriptor(
  name='GammaPoisson',
  full_name='protobuf.distributions.GammaPoisson',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='alpha', full_name='protobuf.distributions.GammaPoisson.alpha', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='inv_beta', full_name='protobuf.distributions.GammaPoisson.inv_beta', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GAMMAPOISSON_GROUP, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=540,
  serialized_end=642,
)


_NORMALINVERSECHISQ_GROUP = descriptor.Descriptor(
  name='Group',
  full_name='protobuf.distributions.NormalInverseChiSq.Group',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='count', full_name='protobuf.distributions.NormalInverseChiSq.Group.count', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mean', full_name='protobuf.distributions.NormalInverseChiSq.Group.mean', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count_times_variance', full_name='protobuf.distributions.NormalInverseChiSq.Group.count_times_variance', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=723,
  serialized_end=789,
)

_NORMALINVERSECHISQ = descriptor.Descriptor(
  name='NormalInverseChiSq',
  full_name='protobuf.distributions.NormalInverseChiSq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='mu', full_name='protobuf.distributions.NormalInverseChiSq.mu', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='kappa', full_name='protobuf.distributions.NormalInverseChiSq.kappa', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sigmasq', full_name='protobuf.distributions.NormalInverseChiSq.sigmasq', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nu', full_name='protobuf.distributions.NormalInverseChiSq.nu', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_NORMALINVERSECHISQ_GROUP, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=645,
  serialized_end=789,
)

_CLUSTERING_PITMANYOR.containing_type = _CLUSTERING;
_CLUSTERING_LOWENTROPY.containing_type = _CLUSTERING;
_CLUSTERING.fields_by_name['pitman_yor'].message_type = _CLUSTERING_PITMANYOR
_CLUSTERING.fields_by_name['low_entropy'].message_type = _CLUSTERING_LOWENTROPY
_BETABERNOULLI_GROUP.containing_type = _BETABERNOULLI;
_DIRICHLETDISCRETE_GROUP.containing_type = _DIRICHLETDISCRETE;
_DIRICHLETPROCESSDISCRETE_GROUP.containing_type = _DIRICHLETPROCESSDISCRETE;
_GAMMAPOISSON_GROUP.containing_type = _GAMMAPOISSON;
_NORMALINVERSECHISQ_GROUP.containing_type = _NORMALINVERSECHISQ;
DESCRIPTOR.message_types_by_name['Clustering'] = _CLUSTERING
DESCRIPTOR.message_types_by_name['BetaBernoulli'] = _BETABERNOULLI
DESCRIPTOR.message_types_by_name['DirichletDiscrete'] = _DIRICHLETDISCRETE
DESCRIPTOR.message_types_by_name['DirichletProcessDiscrete'] = _DIRICHLETPROCESSDISCRETE
DESCRIPTOR.message_types_by_name['GammaPoisson'] = _GAMMAPOISSON
DESCRIPTOR.message_types_by_name['NormalInverseChiSq'] = _NORMALINVERSECHISQ

class Clustering(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class PitmanYor(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CLUSTERING_PITMANYOR
    
    # @@protoc_insertion_point(class_scope:protobuf.distributions.Clustering.PitmanYor)
  
  class LowEntropy(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CLUSTERING_LOWENTROPY
    
    # @@protoc_insertion_point(class_scope:protobuf.distributions.Clustering.LowEntropy)
  DESCRIPTOR = _CLUSTERING
  
  # @@protoc_insertion_point(class_scope:protobuf.distributions.Clustering)

class BetaBernoulli(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Group(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _BETABERNOULLI_GROUP
    
    # @@protoc_insertion_point(class_scope:protobuf.distributions.BetaBernoulli.Group)
  DESCRIPTOR = _BETABERNOULLI
  
  # @@protoc_insertion_point(class_scope:protobuf.distributions.BetaBernoulli)

class DirichletDiscrete(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Group(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _DIRICHLETDISCRETE_GROUP
    
    # @@protoc_insertion_point(class_scope:protobuf.distributions.DirichletDiscrete.Group)
  DESCRIPTOR = _DIRICHLETDISCRETE
  
  # @@protoc_insertion_point(class_scope:protobuf.distributions.DirichletDiscrete)

class DirichletProcessDiscrete(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Group(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _DIRICHLETPROCESSDISCRETE_GROUP
    
    # @@protoc_insertion_point(class_scope:protobuf.distributions.DirichletProcessDiscrete.Group)
  DESCRIPTOR = _DIRICHLETPROCESSDISCRETE
  
  # @@protoc_insertion_point(class_scope:protobuf.distributions.DirichletProcessDiscrete)

class GammaPoisson(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Group(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _GAMMAPOISSON_GROUP
    
    # @@protoc_insertion_point(class_scope:protobuf.distributions.GammaPoisson.Group)
  DESCRIPTOR = _GAMMAPOISSON
  
  # @@protoc_insertion_point(class_scope:protobuf.distributions.GammaPoisson)

class NormalInverseChiSq(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Group(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _NORMALINVERSECHISQ_GROUP
    
    # @@protoc_insertion_point(class_scope:protobuf.distributions.NormalInverseChiSq.Group)
  DESCRIPTOR = _NORMALINVERSECHISQ
  
  # @@protoc_insertion_point(class_scope:protobuf.distributions.NormalInverseChiSq)

# @@protoc_insertion_point(module_scope)