from typing import Any, Dict, Optional

WORDING : Dict[str, Any] =\
{
	'conda_not_activated': '未激活 Conda',
	'python_not_supported': 'Python 版本不受支持，请升级至 {version} 或更高版本',
	'ffmpeg_not_installed': '未安装 FFMpeg',
	'creating_temp': '正在创建临时资源',
	'extracting_frames': '提取帧，分辨率为 {resolution}，每秒 {fps} 帧',
	'extracting_frames_succeed': '提取帧成功',
	'extracting_frames_failed': '提取帧失败',
	'analysing': '正在分析',
	'processing': '正在处理',
	'downloading': '正在下载',
	'temp_frames_not_found': '未找到临时帧',
	'copying_image': '复制图像，分辨率为 {resolution}',
	'copying_image_succeed': '复制图像成功',
	'copying_image_failed': '复制图像失败',
	'finalizing_image': '正在完成图像，分辨率为 {resolution}',
	'finalizing_image_succeed': '完成图像成功',
	'finalizing_image_skipped': '跳过完成图像',
	'merging_video': '合并视频，分辨率为 {resolution}，每秒 {fps} 帧',
	'merging_video_succeed': '合并视频成功',
	'merging_video_failed': '合并视频失败',
	'skipping_audio': '跳过音频',
	'restoring_audio_succeed': '恢复音频成功',
	'restoring_audio_skipped': '跳过恢复音频',
	'clearing_temp': '正在清除临时资源',
	'processing_stopped': '处理已停止',
	'processing_image_succeed': '图像处理成功，耗时 {seconds} 秒',
	'processing_image_failed': '图像处理失败',
	'processing_video_succeed': '视频处理成功，耗时 {seconds} 秒',
	'processing_video_failed': '视频处理失败',
	'model_download_not_done': '模型下载未完成',
	'model_file_not_present': '模型文件不存在',
	'select_image_source': '选择源图像路径',
	'select_audio_source': '选择音频路径',
	'select_video_target': '选择目标视频路径',
	'select_image_or_video_target': '选择目标图像或视频路径',
	'select_file_or_directory_output': '选择输出文件或目录路径',
	'no_source_face_detected': '未检测到源人脸',
	'frame_processor_not_loaded': '无法加载帧处理器 {frame_processor}',
	'frame_processor_not_implemented': '帧处理器 {frame_processor} 未正确实现',
	'ui_layout_not_loaded': '无法加载 UI 布局 {ui_layout}',
	'ui_layout_not_implemented': 'UI 布局 {ui_layout} 未正确实现',
	'stream_not_loaded': '无法加载流 {stream_mode}',
	'point': '.',
	'comma': ',',
	'colon': ':',
	'question_mark': '?',
	'exclamation_mark': '!',
	'help':
	{
		# 安装程序
		'install_dependency': '选择要安装的 {dependency} 变体',
		'skip_conda': '跳过 Conda 环境检查',
		# 通用
		'source': '选择单个或多个源图像或音频',
		'target': '选择单个目标图像或视频',
		'output': '指定输出文件或目录',
		# 杂项
		'force_download': '强制自动下载并退出',
		'skip_download': '省略自动下载和远程查找',
		'headless': '在无用户界面下运行程序',
		'log_level': '调整终端中显示的消息严重程度',
		# 执行
		'execution_providers': '使用不同提供商加速模型推理（选择: {choices}，...）',
		'execution_thread_count': '在处理时指定并行线程数',
		'execution_queue_count': '指定每个线程正在处理的帧数',
		# 内存
		'video_memory_strategy': '平衡快速帧处理和低 VRAM 使用率',
		'system_memory_limit': '限制可用于处理的可用 RAM',
		# 人脸分析器
		'face_analyser_order': '指定人脸分析器检测人脸的顺序',
		'face_analyser_age': '根据年龄筛选检测到的人脸',
		'face_analyser_gender': '根据性别筛选检测到的人脸',
		'face_detector_model': '选择负责检测人脸的模型',
		'face_detector_size': '指定提供给人脸检测器的帧大小',
		'face_detector_score': '根据置信度分数过滤检测到的人脸',
		'face_landmarker_score': '根据置信度分数过滤检测到的人脸标记',
		# 人脸选择器
		'face_selector_mode': '使用基于参考的跟踪或简单匹配',
		'reference_face_position': '指定用于创建参考人脸的位置',
		'reference_face_distance': '指定参考人脸与目标人脸之间的期望相似度',
		'reference_frame_number': '指定用于创建参考人脸的帧',
		# 人脸遮罩
		'face_mask_types': '混合和匹配不同的面罩类型（选择: {choices}）',
		'face_mask_blur': '指定应用于盒状遮罩的模糊程度',
		'face_mask_padding': '向盒状遮罩应用上、右、下和左填充',
		'face_mask_regions': '选择用于区域遮罩的面部特征（选择: {choices}）',
		# 帧提取
		'trim_frame_start': '指定目标视频的起始帧',
	    'trim_frame_end': '指定目标视频的结束帧',
		'temp_frame_format': '指定临时资源的格式',
		'keep_temp': '在处理后保留临时资源',
		# 输出创建
		'output_image_quality': '指定图像质量，这将转化为压缩系数',
		'output_image_resolution': '根据目标图像指定图像输出分辨率',
		'output_video_encoder': '指定用于视频压缩的编码器',
		'output_video_preset': '平衡快速视频处理和视频文件大小',
		'output_video_quality': '指定视频质量，这将转化为压缩系数',
		'output_video_resolution': '根据目标视频指定视频输出分辨率',
		'output_video_fps': '根据目标视频指定视频输出帧率',
		'skip_audio': '从目标视频中省略音频',
		# 帧处理器
		'frame_processors': '加载单个或多个帧处理器（选择: {choices}，...）',
		'face_debugger_items': '加载单个或多个帧处理器（选择: {choices}）',
		'face_enhancer_model': '选择负责增强人脸的模型',
		'face_enhancer_blend': '将增强的人脸混合到之前的人脸中',
		'face_swapper_model': '选择负责交换人脸的模型',
		'frame_colorizer_model': '选择负责给帧上色的模型',
		'frame_colorizer_blend': '将上色的帧混合到之前的帧中',
		'frame_colorizer_size': '指定提供给帧上色器的帧大小',
		'frame_enhancer_model': '选择负责增强帧的模型',
		'frame_enhancer_blend': '将增强的帧混合到之前的帧中',
		'lip_syncer_model': '选择负责同步嘴唇的模型',
		# UI
		'ui_layouts': '启动单个或多个 UI 布局（选择: {choices}，...）'
	},
	'uis':
	{
		# 通用
		'start_button': '开始',
		'stop_button': '停止',
		'clear_button': '清除',
		# 关于
		'donate_button': '捐赠',
		# 基准
		'benchmark_results_dataframe': '基准结果',
		# 基准选项
		'benchmark_runs_checkbox_group': '基准运行',
		'benchmark_cycles_slider': '基准周期',
		# 公共选项
		'common_options_checkbox_group': '选项',
		# 执行
		'execution_providers_checkbox_group': '执行提供商',
		# 执行队列计数
		'execution_queue_count_slider': '执行队列计数',
		# 执行线程计数
		'execution_thread_count_slider': '执行线程计数',
		# 人脸分析器
		'face_analyser_order_dropdown': '人脸分析器顺序',
		'face_analyser_age_dropdown': '人脸分析器年龄',
		'face_analyser_gender_dropdown': '人脸分析器性别',
		'face_detector_model_dropdown': '人脸检测器模型',
		'face_detector_size_dropdown': '人脸检测器大小',
		'face_detector_score_slider': '人脸检测器分数',
		'face_landmarker_score_slider': '人脸标记器分数',
		# 人脸遮罩器
		'face_mask_types_checkbox_group': '人脸遮罩类型',
		'face_mask_blur_slider': '人脸遮罩模糊',
		'face_mask_padding_top_slider': '人脸遮罩上填充',
		'face_mask_padding_right_slider': '人脸遮罩右填充',
		'face_mask_padding_bottom_slider': '人脸遮罩下填充',
		'face_mask_padding_left_slider': '人脸遮罩左填充',
		'face_mask_region_checkbox_group': '人脸遮罩区域',
		# 人脸选择器
		'face_selector_mode_dropdown': '人脸选择器模式',
		'reference_face_gallery': '参考人脸',
		'reference_face_distance_slider': '参考人脸距离',
		# 帧处理器
		'frame_processors_checkbox_group': '帧处理器',
		# 帧处理器选项
		'face_debugger_items_checkbox_group': '人脸调试器项目',
		'face_enhancer_model_dropdown': '人脸增强器模型',
		'face_enhancer_blend_slider': '人脸增强器混合',
		'face_swapper_model_dropdown': '人脸交换器模型',
		'frame_colorizer_model_dropdown': '帧上色器模型',
		'frame_colorizer_blend_slider': '帧上色器混合',
		'frame_colorizer_size_dropdown': '帧上色器大小',
		'frame_enhancer_model_dropdown': '帧增强器模型',
		'frame_enhancer_blend_slider': '帧增强器混合',
		'lip_syncer_model_dropdown': '嘴唇同步器模型',
		# 内存
		'video_memory_strategy_dropdown': '视频内存策略',
		'system_memory_limit_slider': '系统内存限制',
		# 输出
		'output_image_or_video': '输出',
		# 输出选项
		'output_path_textbox': '输出路径',
		'output_image_quality_slider': '输出图像质量',
		'output_image_resolution_dropdown': '输出图像分辨率',
		'output_video_encoder_dropdown': '输出视频编码器',
	    'output_video_preset_dropdown': '输出视频预设',
		'output_video_quality_slider': '输出视频质量',
		'output_video_resolution_dropdown': '输出视频分辨率',
		'output_video_fps_slider': '输出视频帧率',
		# 预览
		'preview_image': '预览',
		'preview_frame_slider': '预览帧',
		# 源
		'source_file': '源',
		# 目标
		'target_file': '目标',
		# 临时帧
		'temp_frame_format_dropdown': '临时帧格式',
		# 裁剪帧
		'trim_frame_start_slider': '裁剪帧开始',
		'trim_frame_end_slider': '裁剪帧结束',
		# 摄像头
		'webcam_image': '网络摄像头',
		# 摄像头选项
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
