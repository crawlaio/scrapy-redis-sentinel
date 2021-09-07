.PHONY: clean sdist upload

sdist:
	python setup.py sdist bdist_wheel --universa

upload:
	python setup.py upload

clean:
	rm -rf build scrapy_redis_sentinel.egg-info dist