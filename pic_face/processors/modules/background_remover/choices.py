from typing import List, Sequence, get_args

from pic_face.common_helper import create_int_range
from pic_face.processors.modules.background_remover.types import BackgroundRemoverModel

background_remover_models : List[BackgroundRemoverModel] = list(get_args(BackgroundRemoverModel))

background_remover_color_range : Sequence[int] = create_int_range(0, 255, 1)
