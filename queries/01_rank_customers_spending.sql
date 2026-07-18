WITH ranks AS (
	SELECT 
		CustomerNo,
		SUM(Price * Quantity) TotalSpend,
		RANK() OVER (ORDER BY SUM(Price * Quantity) DESC) AS rnk
	FROM dbo.sales
	WHERE CustomerNo IS NOT NULL
	GROUP BY CustomerNo
)
SELECT rnk, CustomerNo, TotalSpend
FROM ranks
WHERE rnk < 6
ORDER BY rnk