from typing import Any, Dict, Optional

WORDING : Dict[str, Any] =\
{
	'conda_not_activated': 'Conda 未激活',
	'python_not_supported': '不支持的 Python 版本，请升级到 {version} 或更高版本',
	'ffmpeg_not_installed': 'FFMpeg 未安装',
	'creating_temp': '正在创建临时资源',
	'extracting_frames': '以 {resolution} 的分辨率和每秒 {fps} 帧的速度提取帧',
	'extracting_frames_succeed': '提取帧成功',
	'extracting_frames_failed': '提取帧失败',
	'analysing': '正在分析',
	'processing': '正在处理',
	'downloading': '正在下载',
	'temp_frames_not_found': '未找到临时帧',
	'copying_image': '正在复制分辨率为 {resolution} 的图像',
	'copying_image_succeed': '复制图像成功',
	'copying_image_failed': '复制图像失败',
	'finalizing_image': '正在完成分辨率为 {resolution} 的图像',
	'finalizing_image_succeed': '完成图像成功',
	'finalizing_image_skipped': '跳过完成图像',
	'merging_video': '正在合并分辨率为 {resolution} 和每秒 {fps} 帧的视频',
	'merging_video_succeed': '合并视频成功',
	'merging_video_failed': '合并视频失败',
	'skipping_audio': '跳过音频',
	'restoring_audio_succeed': '恢复音频成功',
	'restoring_audio_skipped': '跳过恢复音频',
	'clearing_temp': '正在清理临时资源',
	'processing_stopped': '处理已停止',
	'processing_image_succeed': '在 {seconds} 秒内处理图像成功',
	'processing_image_failed': '处理图像失败',
	'processing_video_succeed': '在 {seconds} 秒内处理视频成功',
	'processing_video_failed': '处理视频失败',
	'model_download_not_done': '模型下载未完成',
	'model_file_not_present': '模型文件不存在',
	'select_image_source': '选择源路径的图像',
	'select_audio_source': '选择源路径的音频',
	'select_video_target': '选择目标路径的视频',
	'select_image_or_video_target': '选择目标路径的图像或视频',
	'select_file_or_directory_output': '选择输出路径的文件或目录',
	'no_source_face_detected': '未检测到源脸',
	'frame_processor_not_loaded': '无法加载帧处理器 {frame_processor}',
	'frame_processor_not_implemented': '帧处理器 {frame_processor} 实现不正确',
	'ui_layout_not_loaded': '无法加载 UI 布局 {ui_layout}',
	'ui_layout_not_implemented': 'UI 布局 {ui_layout} 实现不正确',
	'stream_not_loaded': '无法加载流 {stream_mode}',
	'point': '.',
	'comma': ',',
	'colon': ':',
	'question_mark': '?',
	'exclamation_mark': '!',
	'help':
	{
		'install_dependency': '选择要安装的 {dependency} 变体',
		'skip_conda': '跳过 conda 环境检查',
		'source': '选择单个或多个源图像或音频',
		'target': '选择单个目标图像或视频',
		'output': '指定输出文件或目录',
		'force_download': '强制自动下载并退出',
		'skip_download': '省略自动下载和远程查找',
		'headless': '在没有用户界面的情况下运行程序',
		'log_level': '调整终端显示的消息严重程度',
		'execution_providers': '使用不同的提供者加速模型推理（选择：{choices}，...）',
		'execution_thread_count': '指定处理时的并行线程数量',
		'execution_queue_count': '指定每个线程处理的帧数',
		'video_memory_strategy': '平衡快速帧处理和低显存使用',
		'system_memory_limit': '限制处理时可用的 RAM',
		'face_analyser_order': '指定面部分析器检测面部的顺序',
		'face_analyser_age': '根据年龄过滤检测到的面部',
		'face_analyser_gender': '根据性别过滤检测到的面部',
		'face_detector_model': '选择负责检测面部的模型',
		'face_detector_size': '指定提供给面部检测器的帧大小',
		'face_detector_score': '根据置信度分数过滤检测到的面部',
		'face_landmarker_score': '根据置信度分数过滤检测到的标志点',
		'face_selector_mode': '使用基于参考的跟踪或简单匹配',
		'reference_face_position': '指定用于创建参考面部的位置',
		'reference_face_distance': '指定参考面部和目标面部之间的相似度',
		'reference_frame_number': '指定用于创建参考面部的帧',
		'face_mask_types': '混合和匹配不同的面部掩码类型（选择：{choices}）',
		'face_mask_blur': '指定应用于框掩码的模糊程度',
		'face_mask_padding': '应用于框掩码的上、右、下和左填充',
		'face_mask_regions': '选择用于区域掩码的面部特征（选择：{choices}）',
		'trim_frame_start': '指定目标视频的起始帧',
		'trim_frame_end': '指定目标视频的结束帧',
		'temp_frame_format': '指定临时资源格式',
		'keep_temp': '处理后保留临时资源',
		'output_image_quality': '指定图像质量，这会转换为压缩因子',
		'output_image_resolution': '根据目标图像指定图像输出分辨率',
		'output_video_encoder': '指定用于视频压缩的编码器',
		'output_video_preset': '平衡快速视频处理和视频文件大小',
		'output_video_quality': '指定视频质量，这会转换为压缩因子',
		'output_video_resolution': '根据目标视频指定视频输出分辨率',
		'output_video_fps': '根据目标视频指定视频输出帧率',
		'skip_audio': '省略目标视频的音频',
		'frame_processors': '加载单个或多个帧处理器（选择：{choices}，...）',
		'face_debugger_items': '加载单个或多个帧处理器（选择：{choices}）',
		'face_enhancer_model': '选择负责增强面部的模型',
		'face_enhancer_blend': '将增强的面部与之前的面部混合',
		'face_swapper_model': '选择负责交换面部的模型',
		'frame_colorizer_model': '选择负责为帧上色的模型',
		'frame_colorizer_blend': '将上色的帧与之前的帧混合',
		'frame_enhancer_model': '选择负责增强帧的模型',
		'frame_enhancer_blend': '将增强的帧与之前的帧混合',
		'lip_syncer_model': '选择负责同步嘴唇的模型',
		'ui_layouts': '启动单个或多个 UI 布局（选择：{choices}，...）'
	},
	'uis':
	{
		'start_button': '开始',
		'stop_button': '停止',
		'clear_button': '清除',
		'donate_button': '捐赠',
		'benchmark_results_dataframe': '基准测试结果',
		'benchmark_runs_checkbox_group': '基准测试运行',
		'benchmark_cycles_slider': '基准测试循环',
		'common_options_checkbox_group': '选项',
		'execution_providers_checkbox_group': '执行提供者',
		'execution_queue_count_slider': '执行队列计数',
		'execution_thread_count_slider': '执行线程计数',
		'face_analyser_order_dropdown': '面部分析器顺序',
		'face_analyser_age_dropdown': '面部分析器年龄',
		'face_analyser_gender_dropdown': '面部分析器性别',
		'face_detector_model_dropdown': '面部检测器模型',
		'face_detector_size_dropdown': '面部检测器大小',
		'face_detector_score_slider': '面部检测器得分',
		'face_landmarker_score_slider': '面部标志点得分',
		'face_mask_types_checkbox_group': '面部掩码类型',
		'face_mask_blur_slider': '面部掩码模糊',
		'face_mask_padding_top_slider': '面部掩码顶部填充',
		'face_mask_padding_right_slider': '面部掩码右侧填充',
		'face_mask_padding_bottom_slider': '面部掩码底部填充',
		'face_mask_padding_left_slider': '面部掩码左侧填充',
		'face_mask_region_checkbox_group': '面部掩码区域',
		'face_selector_mode_dropdown': '面部选择器模式',
		'reference_face_gallery': '参考面部',
		'reference_face_distance_slider': '参考面部距离',
		'frame_processors_checkbox_group': '帧处理器',
		'face_debugger_items_checkbox_group': '面部调试器项目',
		'face_enhancer_model_dropdown': '面部增强器模型',
		'face_enhancer_blend_slider': '面部增强混合',
		'face_swapper_model_dropdown': '面部交换器模型',
		'frame_colorizer_model_dropdown': '帧上色器模型',
		'frame_colorizer_blend_slider': '帧上色混合',
		'frame_enhancer_model_dropdown': '帧增强器模型',
		'frame_enhancer_blend_slider': '帧增强混合',
		'lip_syncer_model_dropdown': '嘴唇同步器模型',
		'video_memory_strategy_dropdown': '视频内存策略',
		'system_memory_limit_slider': '系统内存限制',
		'output_image_or_video': '输出',
		'output_path_textbox': '输出路径',
		'output_image_quality_slider': '输出图像质量',
		'output_image_resolution_dropdown': '输出图像分辨率',
		'output_video_encoder_dropdown': '输出视频编码器',
		'output_video_preset_dropdown': '输出视频预设',
		'output_video_quality_slider': '输出视频质量',
		'output_video_resolution_dropdown': '输出视频分辨率',
		'output_video_fps_slider': '输出视频帧率',
		'preview_image': '预览',
		'preview_frame_slider': '预览帧',
		'source_file': '源',
		'target_file': '目标',
		'temp_frame_format_dropdown': '临时帧格式',
		'trim_frame_start_slider': '修剪帧开始',
		'trim_frame_end_slider': '修剪帧结束',
		'webcam_image': '网络摄像头',
		'webcam_mode_radio': '网络摄像头模式',
		'webcam_resolution_dropdown': '网络摄像头分辨率',
		'webcam_fps_slider': '网络摄像头帧率'
	}
}


def get(key : str) -> Optional[str]:
	if '.' in key:
		section, name = key.split('.')
		if section in WORDING and name in WORDING[section]:
			return WORDING[section][name]
	if key in WORDING:
		return WORDING[key]
	return None
