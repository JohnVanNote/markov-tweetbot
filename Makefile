# Makefile
#
# @author John Van Note <johnlvannote@protonmail.com>
#

.SILENT: run tweet
.PHONY: run

EXEC_PY := python
TEXT_FILE_STORAGE := store_tweets.txt

markov_ds = MarkovChain.py
reader = consume_tweets.py
main = markov.py
send = send_tweet.py

srcfiles = \
	$(markov_ds) \
	$(reader) \
	$(main) \
	$(send)

all: init tweet

init: 
	pip install -r requirements.txt

lint:
	echo "Linting $(srcfiles)"
	for src in $(srcfiles); do \
		pylint $$src; \
		done

store_in_file:
	make run > $(TEXT_FILE_STORAGE)

tweet:
	$(EXEC_PY) $(send)

clean :
	rm -f *.pyc
