import sqlite3
import numpy as np
import matplotlib.pyplot as plt
print(sqlite3.sqlite_version)
conn = sqlite3.connect(r"C:\Users\irisy\Downloads\r33_1.db")
cursor = conn.cursor()

cursor.execute("""
            SELECT left_compliance_values, left_pressure_values
            FROM mhealth
            WHERE subject_id = 538""")
comp_value, press_value = cursor.fetchone()
comp_arr = np.array(comp_value.split("|"), dtype=float)
press_arr = np.array(press_value.split("|"), dtype=float)

print(comp_arr.size)
print(press_arr.size)
conn.close()
d = np.diff(press_arr)

print("min step:", d.min())
print("max step:", d.max())
print("unique steps:", np.unique(np.round(d, 6))[:20])
print("all equal:", np.allclose(d, d[0]))
plt.scatter(press_arr, comp_arr)
plt.xlabel("Pressure (da Pa)")
plt.ylabel("Compliance (cm^3)")
plt.show()
