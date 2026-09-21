IF NOT EXISTS (
    SELECT 1 
    FROM sys.schemas 
    WHERE 
		name = 'Analytics'
)
BEGIN
    EXEC('CREATE SCHEMA Analytics')
END
GO