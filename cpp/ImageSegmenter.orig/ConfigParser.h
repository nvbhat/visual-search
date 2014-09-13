# pragma once
#include <map>
#include <fstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;
class ConfigParser {
private:
	bool m_error_state;
	vector<string> m_paramLines;
	map<string, string> m_paramList;

	vector<string> SplitString(string str, const string &delim);
public:
	ConfigParser();
	bool good() { return (m_error_state==false); }
	bool ContainsParam(const string& key) { return (m_paramList.find(key) != m_paramList.end()); }
	string GetParamValue(const string& key) { return m_paramList[key]; }
	void ReadParamFile(const string& param_file_path);
};