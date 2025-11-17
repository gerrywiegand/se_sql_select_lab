
SELECT jobTitles
        WHEN 'President' THEN 'Executive'
        WHEN 'VP Sales' THEN 'Executive'
        WHEN 'VP Marketing' THEN 'Executive'
        ELSE 'Not Executive'
        END AS 'role'
    FROM employees
    