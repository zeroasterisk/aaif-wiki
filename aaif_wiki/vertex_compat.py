"""Environment fix-ups needed before constructing a Vertex client.

Isolated here so the workaround is discoverable rather than buried in the curator.

**The mTLS trap.** ``google-auth`` will try to open a mutual-TLS channel whenever
it discovers a client certificate config (commonly ``/etc/gcloud/certificate_config.json``
on managed corporate workstations), *even when* ``GOOGLE_API_USE_CLIENT_CERTIFICATE``
is unset. If the enterprise cert provider binary then fails -- on the machine this
was developed on it segfaults, surfacing as ``Cert provider command returns
non-zero status code -11`` -- every Vertex call dies with ``MutualTLSChannelError``,
despite ADC being perfectly valid. A raw ``curl`` with the same token succeeds,
which makes the failure look like an SDK bug rather than a transport one.

Setting the variable explicitly to ``"false"`` opts out of the mTLS path. We only
set it when the caller has expressed no preference, so anyone who genuinely needs
mTLS keeps it by setting the variable themselves.
"""

from __future__ import annotations

import os

MTLS_ENV = "GOOGLE_API_USE_CLIENT_CERTIFICATE"


def prepare_environment() -> dict[str, str]:
    """Apply compatibility defaults. Returns a description of what was changed."""
    applied: dict[str, str] = {}
    if not os.environ.get(MTLS_ENV):
        os.environ[MTLS_ENV] = "false"
        applied[MTLS_ENV] = "false"
    return applied
