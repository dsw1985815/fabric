from invocations.docs import docs, www
from invocations import packaging

from invoke import Collection


ns = Collection(docs, www, release=packaging)
