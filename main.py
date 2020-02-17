from videocr import utils
from videocr.video import Video


def get_subtitles(
        video_path: str, lang='eng', time_start='0:00', time_end='',
        conf_threshold=65, sim_threshold=90, use_fullframe=False,
        width_boundary: tuple=None, height_boundary: tuple=None, img_path: str=None) -> str:
    utils.download_lang_data(lang)

    v = Video(video_path)
    v.run_ocr(lang, time_start, time_end, conf_threshold, use_fullframe, width_boundary, height_boundary, img_path)
    # return v.get_subtitles(sim_threshold)

if __name__ == "__main__":
    import sys

    argv = sys.argv
    get_subtitles(sys.argv[1], "chi_sim", '3:46', '3:47', height_boundary=(600, 660), width_boundary=(160, 1280), img_path=sys.argv[2])