#!/usr/bin/env python
# -*- coding: utf-8 -*-

sum([int(i) for i in str(reduce(lambda x, y:x * y, range(1, 101)))])
