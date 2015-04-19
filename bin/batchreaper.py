#!/usr/bin/env python

import batchreaper

parser = batchreaper.setup_parser()
opts = batchreaper.parse_args()
batchreaper.batchreaper(opts.input, opts.output)