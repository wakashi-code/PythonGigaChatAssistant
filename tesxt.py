import os

# global GIGACHAT_CREDENTIALS, GIGACHAT_SCOPE, GIGACHAT_MODEL
#
# os.environ ["GIGACHAT_CREDENTIALS"] = "eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.eiRJN-QBp13y-bzVU3GaN5aFUgamTuh0ERV243mqQiX0DXXbygaUyhRS2Rfqk5DLK75uOtLEpY-tm1fbyOw4fgplFzHB-zArqQjLbB_K2asK6Aj2RBLeIdQy0_up88vryau1CTdClRKsAI452cyaFQVOnzYe50M7o5kCQtTi7l6NTtW6a579oVmKHVp_3zLvg0OqF_9dV92_Nhos2WbZgx0YqDunsHDHca8WYUfORJEbzSW6iOMrnmmRV9idKLPUq2RSUZbUrTS39KBUGyNPJ9nUxLqjQ8WYZMjl9n0cXtcJsRiZWU_x6zgFU91A3oKwK6Keb6DuzHlMk5FGAOB0pA.BXXmshxWa3SZ44qtbnA5mw.ZZfXAaaJBpc1TUzCB2YMRbChKmn8pl8FvvYZzZfLzslVyXd_BEW8Cm-XBGVdAdG-B457T5OEHcNjiqWwavCiXLh59xAxxQNuiMNYoFJtC_FqCNBvVNyWyVEFOnsN7iC2yLjJ2x9AJBmyn_f26fzdfNoQEARphSTCU_qNMwIllL0qZDUZF3-pkPiJvu5aLJJcPcjw8oZJs0LSf6sTPj_ZtODnhnhrUWwftbkkk620hZHMOVM7bJXr7R3yhV_I9ozcGlwEJ24Es4sT80LBPm2avn-njOeqDRCfq-jZ6l_BRlSBKYhfJc1kU6PvNSSy22sa2_YeiroAvHv9HsrFoglDkv7Y4UowX5SuukCMhfnURFkFF4amyxXJ3QGc37L2nH1l-_iuRdF-j_1YBgJblu5KU91ZyzM6q4iSIm2xLsCV19bCbL_2u8R14csutkH9FSUJM9aZ4H7B-A6p0FYpB5hN1vNIHKC68Zpx1qRlSuydyc6SiPHClCa1MesGxwqWj0UmUGu9K6PHoSrq_wLE_v438Ubp8zMWvrEniDqZ5yefgI_0ldWwcuR-Jb7mur-HbfBzAVR0QBXctDka8VLbP5mNW_IM8LEBRo06mP2KnHLpK5L9cN1ew44gOJv9hQuosav9J_BHiHaCsdJ4w4wBMRUz7UTLZHQjAM2xL-WZ5kW3xSarKV6PoQQuQw86ua3rz_JpgjO8nUJMqGKtkP8yH5hZ9SjtojmtinlOkhOkjbZ_X4E.J6pPF72LK-PgyrD6is2yInlWLoIQKT5W-xI0Ccn6gMQ"
# os.environ["GIGACHAT_SCOPE"] = "GIGACHAT_API_PERS"
# os.environ["GIGACHAT_MODEL"] = "GigaChat"
#
#
# print(os.getenv("GIGACHAT_CREDENTIALS"))
# print(os.getenv("GIGACHAT_SCOPE"))
# print(os.getenv("GIGACHAT_MODEL"))


GIGACHAT_CREDENTIALS = "eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.eiRJN-QBp13y-bzVU3GaN5aFUgamTuh0ERV243mqQiX0DXXbygaUyhRS2Rfqk5DLK75uOtLEpY-tm1fbyOw4fgplFzHB-zArqQjLbB_K2asK6Aj2RBLeIdQy0_up88vryau1CTdClRKsAI452cyaFQVOnzYe50M7o5kCQtTi7l6NTtW6a579oVmKHVp_3zLvg0OqF_9dV92_Nhos2WbZgx0YqDunsHDHca8WYUfORJEbzSW6iOMrnmmRV9idKLPUq2RSUZbUrTS39KBUGyNPJ9nUxLqjQ8WYZMjl9n0cXtcJsRiZWU_x6zgFU91A3oKwK6Keb6DuzHlMk5FGAOB0pA.BXXmshxWa3SZ44qtbnA5mw.ZZfXAaaJBpc1TUzCB2YMRbChKmn8pl8FvvYZzZfLzslVyXd_BEW8Cm-XBGVdAdG-B457T5OEHcNjiqWwavCiXLh59xAxxQNuiMNYoFJtC_FqCNBvVNyWyVEFOnsN7iC2yLjJ2x9AJBmyn_f26fzdfNoQEARphSTCU_qNMwIllL0qZDUZF3-pkPiJvu5aLJJcPcjw8oZJs0LSf6sTPj_ZtODnhnhrUWwftbkkk620hZHMOVM7bJXr7R3yhV_I9ozcGlwEJ24Es4sT80LBPm2avn-njOeqDRCfq-jZ6l_BRlSBKYhfJc1kU6PvNSSy22sa2_YeiroAvHv9HsrFoglDkv7Y4UowX5SuukCMhfnURFkFF4amyxXJ3QGc37L2nH1l-_iuRdF-j_1YBgJblu5KU91ZyzM6q4iSIm2xLsCV19bCbL_2u8R14csutkH9FSUJM9aZ4H7B-A6p0FYpB5hN1vNIHKC68Zpx1qRlSuydyc6SiPHClCa1MesGxwqWj0UmUGu9K6PHoSrq_wLE_v438Ubp8zMWvrEniDqZ5yefgI_0ldWwcuR-Jb7mur-HbfBzAVR0QBXctDka8VLbP5mNW_IM8LEBRo06mP2KnHLpK5L9cN1ew44gOJv9hQuosav9J_BHiHaCsdJ4w4wBMRUz7UTLZHQjAM2xL-WZ5kW3xSarKV6PoQQuQw86ua3rz_JpgjO8nUJMqGKtkP8yH5hZ9SjtojmtinlOkhOkjbZ_X4E.J6pPF72LK-PgyrD6is2yInlWLoIQKT5W-xI0Ccn6gMQ"
GIGACHAT_SCOPE = "GIGACHAT_API_PERS"
GIGACHAT_MODEL = "GigaChat"

# Вывести значения
print(GIGACHAT_CREDENTIALS)
print(GIGACHAT_SCOPE)
print(GIGACHAT_MODEL)