import os
import sys

from pic_face.types import AppContext


def detect_app_context() -> AppContext:
	jobs_path = os.path.join('pic_face', 'jobs')
	uis_path = os.path.join('pic_face', 'uis')
	frame = sys._getframe(1)

	while frame:
		if jobs_path in frame.f_code.co_filename:
			return 'cli'
		if uis_path in frame.f_code.co_filename:
			return 'ui'
		frame = frame.f_back
	return 'cli'
