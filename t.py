from decord import VideoReader
import torch.utils.dlpack as dlpack

tmp_file = "23.webm"
vr = VideoReader(tmp_file, num_threads=1)
# print("总帧数:", vr.num_frames)
# list_ = [0, 4, 7, 9, 12, 17, 18, 23]
list_ = [0, 4, 7, 9]

frames = dlpack.from_dlpack(vr.get_batch(list_).to_dlpack()).clone()