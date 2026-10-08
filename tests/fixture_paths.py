"""Caller-supplied, locally verified canonical source fixture. Never fetch here."""
import os
from pathlib import Path

SOURCE = Path(os.environ.get('PSTACK_SOURCE_FIXTURE', Path.home() / 'Herd/pstack-port-research/task-1-20261007/extracted/plugins-df581122cde17e6e27686b5a448bde23e4ad4318/pstack')).expanduser()
