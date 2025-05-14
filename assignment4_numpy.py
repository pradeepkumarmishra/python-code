import numpy as np

# Employee Details: Employee ID, Department, Number of Years with AtliQ
employee_details = np.array([
    [101, 'Sales', 3],
    [102, 'HR', 5],
    [103, 'IT', 2],
    [104, 'Sales', 8],
    [105, 'IT', 6],
    [106, 'HR', 4],
    [107, 'IT', 7],
    [108, 'Sales', 1],
    [109, 'HR', 3]
])

# Survey Results: Employee ID, Happiness Score (1-10)
survey_results = np.array([
    [101, 8],
    [102, 10],
    [103, 9],
    [104, 6],
    [105, 7],
    [106, 8],
    [107, 9],
    [108, 5],
    [109, 7]
])

combine_survey = np.hstack((employee_details, survey_results))
#task 1
#print(combine_survey)
#task 2
#print(combine_survey[:,4])
#task 3
#survey_results = survey_results[survey_results[:,1].argsort()]
#print(survey_results)
#task4
#for i in range(0, len(employee_details)):
#print(employee_details[:,:2])
#task5
#print(combine_survey)
#print(combine_survey[:,[0,-1]])
#task 6
#print(combine_survey[:,[0,-1]].astype(float))
#task 7
#print(np.mean(survey_results[:,1]).astype(int))
#task 9
#print(combine_survey[:,1])
hr_dept_data = combine_survey[combine_survey[:,1] == "HR" ][:,-1].astype(float)
#print(hr_dept_data)
print(np.mean(hr_dept_data))



