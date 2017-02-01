import os
import logging
from sys import platform

import pypandoc

log = logging.getLogger(__name__)

def install_pandoc():
    """Installs Pandoc from binary
    
    Internet connection is required"""

    try:
        log.info('Pandoc available with command: %s',
                 pypandoc.get_pandoc_path())
    except:
        download_pandoc()
        log.info('Pandoc is installed and available with command: %s',
                 pypandoc.get_pandoc_path())

def convert(source, to, format, outputfile=None,
            variables={}, encoding='utf-8', extra_args=()):
    """Wrapper around pypandoc.convert()
    
    :param dict variables: dictionary with values for template.
            If some value of dictionary is list every argument
            of it is passed separately to Pandoc"""
    args = []
    args.extend(extra_args)
    for k, v in variables.items():
        if not isinstance(v, list):
            args.extend(['-V', '%s=%s' % (k, v)])
        else:
            for i in v:
                args.extend(['-V', '%s=%s' % (k, i)])
    try:
        return pypandoc.convert_text(source, to, format, extra_args=args,
                                     encoding=encoding, outputfile=outputfile)
    except Exception as e:
        log.error(e)
