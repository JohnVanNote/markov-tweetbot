# Makefile
#
# @author John Van Note <johnlvannote@protonmail.com>
#

.SILENT: run
.PHONY: run

TEXT_FILE_STORAGE := store_tweets.txt

run:
	python consume_tweets.py

store_in_file:
	make run > $(TEXT_FILE_STORAGE)

test_markov:
	python markov.py

test_file:
	python markov.py $(TEXT_FILE_STORAGE)
