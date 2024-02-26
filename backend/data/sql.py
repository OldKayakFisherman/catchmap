statements = {
    'get.user': """
        SELECT * 
        FROM accounts
        WHERE email = %s
    """,
    'add.new.user': """
        INSERT INTO accounts
        (email, credentials, token)
        VALUES(%s, %s, %s)
    """
}