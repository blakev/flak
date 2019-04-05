#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# >>
#   flak, 2019
# <<

import os
import json
from logging import getLogger
from logging.config import dictConfig

import toml
from easydict import EasyDict

from flak.constants import DEFAULT_CONFIG_PATH, DEFAULT_LOGGING_PATH

logger = getLogger('flak.config')


def get_config(path: str) -> EasyDict:
    """Load the configuration file found at ``path``.

    Raises:
        RuntimeError: when no configuration exists at ``path``.
    """
    if not os.path.isfile(path):
        raise RuntimeError('cannot locate config at path, %s' % path)
    with open(path, 'r') as fp:
        conf = toml.load(fp)
    return EasyDict(conf)


config = get_config(os.getenv('FLAK_CONFIG', DEFAULT_CONFIG_PATH))


if config.enable_logging:
    log_config = os.getenv('FLAK_LOGGING_CONFIG', DEFAULT_LOGGING_PATH)
    with open(log_config, 'r') as fp:
        dictConfig(json.load(fp))
