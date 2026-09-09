"""Email-corpus support for auditable, hypothesis-driven swarm research."""
from .corpus import EmailCorpus
from .replay import ReplayCorpus
from .schemas import EmailDocument, EmailSegment, IngestStats
from .stream import ChronologicalSwarm, StreamConfig, StreamOfflineClient

__all__ = ['EmailCorpus', 'EmailDocument', 'EmailSegment', 'IngestStats', 'ReplayCorpus',
           'ChronologicalSwarm', 'StreamConfig', 'StreamOfflineClient']
