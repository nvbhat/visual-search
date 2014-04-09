#include "ConfigParser.h"
#include <fstream>

ConfigParser::ConfigParser()
{
	m_error_state = false;
}

void ConfigParser::ReadParamFile(const string& param_file_path)
{
	ifstream ifs;

	ifs.open(param_file_path.c_str(), ios::in);
	if (!ifs) {
		cerr << "Could not open " << param_file_path << " for reading.\n";
		m_error_state = true;
		return;
	}
	
	string line;
	while (getline(ifs, line)) {
		// If line starts with #, ignore
		if (line[0] == '#')
			continue;
		else {
			vector<string> kvPair = SplitString(line, "=");
			if (!kvPair.empty())
				m_paramList[kvPair.at(0)] = kvPair.at(1);
			else {
				m_error_state = true;
				return;
			}
		}			
	}
	ifs.close();

	

}


vector<string> ConfigParser::SplitString(string str, const string &delim) 
{
	vector<string> result;
	size_t found;
	if ((found = str.find(delim)) != string::npos) {
		result.push_back(str.substr(0, found));
		str = str.substr(found + delim.size());
		result.push_back(str);
	}
	else
		m_error_state = true;

	return result;
}