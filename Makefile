VIDEO_PATH="https://www.youtube.com/watch?v=h4s0llOpKrU"

clean:
	rm -Rf *.egg-info
	rm -Rf build
	rm -Rf dist
	rm -Rf .pytest_cache
	rm -f .coverage

build: clean
	python3 setup.py sdist

run: build
	python3 -m human_detector.main \
	--video_path ${VIDEO_PATH} \
	--mode 'HOG'

linter:
	pip3 install -r requirements.txt
	pip3 install pylint
	pylint human_detector
