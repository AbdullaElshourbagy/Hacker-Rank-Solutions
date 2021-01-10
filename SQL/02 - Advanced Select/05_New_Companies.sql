----https://www.hackerrank.com/challenges/the-company/problem


---Solution


SELECT company.company_code, company.founder, 
      COUNT(DISTINCT leadManager.lead_manager_code),
	  COUNT(DISTINCT seniorManager.senior_manager_code),
      COUNT(DISTINCT manager.manager_code),
	  COUNT(DISTINCT employee.employee_code)
FROM Company company, Lead_Manager leadManager,
     Senior_Manager seniorManager, Manager manager, Employee employee
WHERE company.company_code = leadManager.company_code AND 
      leadManager.lead_manager_code = seniorManager.lead_manager_code AND
      seniorManager.senior_manager_code = manager.senior_manager_code AND
      manager.manager_code = employee.manager_code
GROUP BY company.company_code, company.founder ORDER BY company.company_code;