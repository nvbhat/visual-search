#include "ImageSegmenter.h"

void ImageSegmenter::ReadConfigParams()
{
	if (m_cfgParser.ContainsParam("document-image-path"))
		m_document_image_path = m_cfgParser.GetParamValue("document-image-path");
	if (m_cfgParser.ContainsParam("output-level"))
		m_output_level = m_cfgParser.GetParamValue("output-level");	
	if (m_cfgParser.ContainsParam("output-file-path"))
		m_output_file_path = m_cfgParser.GetParamValue("output-file-path");
	
	if (m_cfgParser.ContainsParam("white-row-fill-factor"))
		m_white_row_fill_factor = atof(m_cfgParser.GetParamValue("white-row-fill-factor").c_str());
	if (m_cfgParser.ContainsParam("white-column-fill-factor"))
		m_white_col_fill_factor = atof(m_cfgParser.GetParamValue("white-column-fill-factor").c_str());

	if (m_cfgParser.ContainsParam("whiten-band-width"))
		m_whiten_band_width = atoi(m_cfgParser.GetParamValue("whiten-band-width").c_str());
	if (m_cfgParser.ContainsParam("whiten-band-height"))
		m_whiten_band_height = atoi(m_cfgParser.GetParamValue("whiten-band-height").c_str());

	if (m_cfgParser.ContainsParam("do-dilation"))
		m_do_dilation = ( atoi(m_cfgParser.GetParamValue("do-dilation").c_str()) == 1 ) ? true : false;

	if (m_cfgParser.ContainsParam("line-element-size"))
		m_line_element_length = atoi( m_cfgParser.GetParamValue("line-element-size").c_str());
	
}