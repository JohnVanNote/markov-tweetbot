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

init: 
	pip install -r requirements.txt

build_chain: 
	$(EXEC_PY) MarkovChain.py

lint:
	echo "Linting $(srcfiles)"
	for src in $(srcfiles); do \
		pylint $$src; \
		done

run:
	$(EXEC_PY) consume_tweets.py

store_in_file:
	make run > $(TEXT_FILE_STORAGE)

test_markov:
	$(EXEC_PY) markov.py

test_file:
	$(EXEC_PY) markov.py $(TEXT_FILE_STORAGE)

tweet:
	$(EXEC_PY) $(send)

clean :
	rm -f *.pyc
