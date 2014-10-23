#!/bin/bash
# Every once in a while, kill all firefox processes since some are still left hanging.
ps aux | grep -ie firefox | awk {'print $2'} | xargs kill -9