import subprocess
import sys

import pytest

from pic_face import ffmpeg, ffmpeg_builder, process_manager
from pic_face.download import conditional_download
from pic_face.jobs.job_manager import clear_jobs, init_jobs
from pic_face.types import Resolution, Scale
from pic_face.vision import detect_image_resolution, detect_video_resolution
from .helper import get_test_example_file, get_test_examples_directory, get_test_jobs_directory, get_test_output_file, prepare_test_output_directory, get_test_example_url


@pytest.fixture(scope = 'module', autouse = True)
def before_all() -> None:
	process_manager.start()
	conditional_download(get_test_examples_directory(),
	[
		get_test_example_url('source.jpg'),
		get_test_example_url('target-240p.mp4')
	])

	ffmpeg.run_ffmpeg(
		ffmpeg_builder.chain(
			ffmpeg_builder.set_input(get_test_example_file('target-240p.mp4')),
			[
				'-vframes',
				'1'
			],
			ffmpeg_builder.set_output(get_test_example_file('target-240p.jpg'))
		)
	)


@pytest.fixture(scope = 'function', autouse = True)
def before_each() -> None:
	clear_jobs(get_test_jobs_directory())
	init_jobs(get_test_jobs_directory())
	prepare_test_output_directory()


@pytest.mark.parametrize('output_image_scale, output_image_resolution',
[
	(0.5, (212, 112)),
	(1.0, (426, 226)),
	(2.0, (852, 452)),
	(8.0, (3408, 1808))
])
def test_output_image_scale(output_image_scale : Scale, output_image_resolution : Resolution) -> None:
	output_file_path = get_test_output_file('test-output-image-scale-' + str(output_image_scale) + '.jpg')
	commands = [ sys.executable, 'pic_face.py', 'headless-run', '--jobs-path', get_test_jobs_directory(), '--processors', 'frame_enhancer', '-t', get_test_example_file('target-240p.jpg'), '-o', output_file_path, '--output-image-scale', str(output_image_scale) ]

	assert subprocess.run(commands).returncode == 0
	assert detect_image_resolution(output_file_path) == output_image_resolution


@pytest.mark.parametrize('output_video_scale, output_video_resolution',
[
	(0.5, (212, 112)),
	(1.0, (426, 226)),
	(2.0, (852, 452)),
	(8.0, (3408, 1808))
])
def test_output_video_scale(output_video_scale : Scale, output_video_resolution : Resolution) -> None:
	output_file_path = get_test_output_file('test-output-video-scale-' + str(output_video_scale) + '.mp4')
	commands = [ sys.executable, 'pic_face.py', 'headless-run', '--jobs-path', get_test_jobs_directory(), '--processors', 'frame_enhancer', '-t', get_test_example_file('target-240p.mp4'), '-o', output_file_path, '--trim-frame-end', '1', '--output-video-scale', str(output_video_scale) ]

	assert subprocess.run(commands).returncode == 0
	assert detect_video_resolution(output_file_path) == output_video_resolution
