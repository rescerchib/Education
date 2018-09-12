import dict

interest = dict.Interest()
print(interest.count())

interest.add("Java", "프로그래밍")
interest.add("인천전자마이스터고등학교", "고등학교")
interest.add("인천하이텍고등학교", "고등학교")

print(interest.count())

print(interest.get_keys())
print(interest.get_values())

interest.write_dict_in_file()
