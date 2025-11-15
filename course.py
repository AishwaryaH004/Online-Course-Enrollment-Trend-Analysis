# # ------MATPLOTLIB-------
#
# import matplotlib.pyplot as plt
# from adjustText import adjust_text
#
# # ----------- Read datasets from Excel -----------
# df_overall = pd.read_excel("course_enrollments_overall.xlsx")
# df_monthly = pd.read_excel("course_enrollments_monthly.xlsx")
# df_yearly = pd.read_excel("course_ratings_yearly.xlsx")
# df_revenue = pd.read_excel("course_revenue_yearly.xlsx")
#
#
# # ------------ Layout Setup ------------
# fig = plt.figure(figsize=(14, 8))
# fig.patch.set_facecolor('#e8f4f8')
#
# # GridSpec for custom layout like friend's
# from matplotlib.gridspec import GridSpec
# gs = GridSpec(2, 2, figure=fig, width_ratios=[1, 1], height_ratios=[1, 1])
# gs.update(wspace=0.35, hspace=0.4)
#
# # ------------ 1. PIE CHART (Top Left) ------------
# ax1 = fig.add_subplot(gs[0, 0])
# month_filter = "January"
# df_month_selected = df_monthly[df_monthly["month"] == month_filter]
# pie_colors = plt.cm.Pastel1.colors
#
# wedges, texts, autotexts = ax1.pie(
#     df_month_selected["enrollments"],
#     labels=df_month_selected["category"],
#     autopct='%1.1f%%',
#     startangle=90,
#     colors=pie_colors,
#     wedgeprops={"edgecolor": "black", 'linewidth': 1.2}
# )
# ax1.set_title(f"Enrollment Share - {month_filter}", fontsize=14, fontweight='bold', color="#333333")
#
# for autotext in autotexts:
#     autotext.set_color("#222222")
#     autotext.set_fontsize(9)
#     autotext.set_weight("bold")
#
# # ------------ 2. BAR CHART (Top Right) ------------
# ax2 = fig.add_subplot(gs[0, 1])
# category_totals = df_overall.groupby("category")["enrollments"].sum().sort_values(ascending=False)
# bars = ax2.bar(category_totals.index, category_totals.values,
#                color="#ff80ab", edgecolor='black', linewidth=1.2)  # Pink
# ax2.set_title("Total Enrollments by Category", fontsize=14, fontweight='bold', color="#333333")
# ax2.set_ylabel("Enrollments", fontsize=12)
# ax2.set_xticks(range(len(category_totals.index)))
# ax2.set_xticklabels(category_totals.index, rotation=45, ha="right", fontsize=10)
#
# for bar in bars:
#     height = bar.get_height()
#     ax2.text(bar.get_x() + bar.get_width()/2, height + 50, str(height),
#              ha='center', va='bottom', fontsize=9, color="#444444")
#
#
# # ------------ 3. LINE CHART (Bottom Left) ------------
# ax3 = fig.add_subplot(gs[1, 0])
#
# df_revenue = df_yearly.groupby("year")["revenue"].sum().reset_index()
#
# ax3.plot(df_revenue["year"], df_revenue["revenue"],
#          marker='o', color='purple', linewidth=2)
#
# ax3.set_title("Revenue Trend Over Years", fontsize=14, fontweight='bold', color="#333333")
# ax3.set_xlabel("Year", fontsize=12)
# ax3.set_ylabel("Total Revenue", fontsize=12)
#
# ax3.set_xticks(df_revenue["year"])
# ax3.set_xticklabels(df_revenue["year"], rotation=45, ha="right", fontsize=10)
#
# ax3.grid(True, linestyle="--", alpha=0.5)
#
#
# # ------------ 4. SCATTER CHART (Bottom Right) ------------
# ax4 = fig.add_subplot(gs[1, 1])
# scatter_colors = plt.cm.plasma(
#     (df_yearly["year"] - df_yearly["year"].min()) /
#     (df_yearly["year"].max() - df_yearly["year"].min())
# )
#
# scatter = ax4.scatter(df_yearly["enrollments"], df_yearly["rating"],
#                       c=scatter_colors, s=120, alpha=0.9,
#                       edgecolor='black', linewidth=1.1)
#
# ax4.set_title("Ratings vs Enrollments", fontsize=14, fontweight='bold', color="#333333")
# ax4.set_xlabel("Enrollments", fontsize=12)
# ax4.set_ylabel("Rating", fontsize=12)
# ax4.grid(True, linestyle="--", alpha=0.5)
#
# texts = []
# for i in range(len(df_yearly)):
#     short_name = " ".join(df_yearly["course_name"][i].split()[:1])  # take first 2 words only
#     texts.append(
#         ax4.text(df_yearly["enrollments"][i],
#                  df_yearly["rating"][i],
#                  short_name,
#                  fontsize=8, color="#8B0000")  # Dark red color
#     )
#
# adjust_text(
#     texts,
#     arrowprops=dict(arrowstyle="->", color='gray', lw=0.6, shrinkA=5, shrinkB=2),
#     expand_points=(1.2, 1.4),
#     ax=ax4
# )
#
# plt.show()




# ------MATPLOTLIB-------

import matplotlib.pyplot as plt
from adjustText import adjust_text
import numpy as np
import pandas as pd

# ----------- Read datasets from Excel -----------
df_overall = pd.read_excel("course_enrollments_overall.xlsx")
df_monthly = pd.read_excel("course_enrollments_monthly.xlsx")
df_yearly = pd.read_excel("course_ratings_yearly.xlsx")
df_revenue = pd.read_excel("course_revenue_yearly.xlsx")

# ------------ Layout Setup ------------
fig = plt.figure(figsize=(14, 8))
fig.patch.set_facecolor('#e8f4f8')

# GridSpec for custom layout like friend's
from matplotlib.gridspec import GridSpec
gs = GridSpec(2, 2, figure=fig, width_ratios=[1, 1], height_ratios=[1, 1])
gs.update(wspace=0.35, hspace=0.4)

# ------------ 1. PIE CHART (Top Left) ------------
ax1 = fig.add_subplot(gs[0, 0])
month_filter = "January"
df_month_selected = df_monthly[df_monthly["month"] == month_filter]
pie_colors = plt.cm.Pastel1.colors

wedges, texts, autotexts = ax1.pie(
    df_month_selected["enrollments"],
    labels=df_month_selected["category"],
    autopct='%1.1f%%',
    startangle=90,
    colors=pie_colors,
    wedgeprops={"edgecolor": "black", 'linewidth': 1.2}
)
ax1.set_title(f"Enrollment Share - {month_filter}", fontsize=14, fontweight='bold', color="#333333")

for autotext in autotexts:
    autotext.set_color("#222222")
    autotext.set_fontsize(9)
    autotext.set_weight("bold")

# ------------ 2. BAR CHART (Top Right) ------------
ax2 = fig.add_subplot(gs[0, 1])
category_totals = df_overall.groupby("category")["enrollments"].sum().sort_values(ascending=False)
bars = ax2.bar(category_totals.index, category_totals.values,
               color="#ff80ab", edgecolor='black', linewidth=1.2)  # Pink
ax2.set_title("Total Enrollments by Category", fontsize=14, fontweight='bold', color="#333333")
ax2.set_ylabel("Enrollments", fontsize=12)
ax2.set_xticks(range(len(category_totals.index)))
ax2.set_xticklabels(category_totals.index, rotation=45, ha="right", fontsize=10)

for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, height + 50, str(height),
             ha='center', va='bottom', fontsize=9, color="#444444")

# ------------ 3. LINE CHART (Bottom Left) ------------
ax3 = fig.add_subplot(gs[1, 0])
df_revenue_grouped = df_yearly.groupby("year")["revenue"].sum().reset_index()

ax3.plot(df_revenue_grouped["year"], df_revenue_grouped["revenue"],
         marker='o', color='purple', linewidth=2)

ax3.set_title("Revenue Trend Over Years", fontsize=14, fontweight='bold', color="#333333")
ax3.set_xlabel("Year", fontsize=12)
ax3.set_ylabel("Total Revenue", fontsize=12)
ax3.set_xticks(df_revenue_grouped["year"])
ax3.set_xticklabels(df_revenue_grouped["year"], rotation=45, ha="right", fontsize=10)
ax3.grid(True, linestyle="--", alpha=0.5)

# ------------ 4. SCATTER CHART (Bottom Right) ------------
ax4 = fig.add_subplot(gs[1, 1])
scatter_colors = plt.cm.plasma(
    (df_yearly["year"] - df_yearly["year"].min()) /
    (df_yearly["year"].max() - df_yearly["year"].min())
)

scatter = ax4.scatter(df_yearly["enrollments"], df_yearly["rating"],
                      c=scatter_colors, s=120, alpha=0.9,
                      edgecolor='black', linewidth=1.1)

ax4.set_title("Ratings vs Enrollments", fontsize=14, fontweight='bold', color="#333333")
ax4.set_xlabel("Enrollments", fontsize=12)
ax4.set_ylabel("Rating", fontsize=12)
ax4.grid(True, linestyle="--", alpha=0.5)

texts = []
for i in range(len(df_yearly)):
    short_name = " ".join(df_yearly["course_name"][i].split()[:1])  # first word only
    texts.append(
        ax4.text(df_yearly["enrollments"][i],
                 df_yearly["rating"][i],
                 short_name,
                 fontsize=8, color="#8B0000")  # Dark red
    )

adjust_text(
    texts,
    arrowprops=dict(arrowstyle="->", color='gray', lw=0.6, shrinkA=5, shrinkB=2),
    expand_points=(1.2, 1.4),
    ax=ax4
)

# ----------- CORRELATION ANALYSIS -----------
print("\n--- CORRELATION ANALYSIS ---")

# 1. Perfect correlation (synthetic example)
perfect_x = np.arange(1, 11)
perfect_y = perfect_x * 2
perfect_corr = np.corrcoef(perfect_x, perfect_y)[0, 1]
print(f"[Perfect Correlation] Coefficient = {perfect_corr:.2f} → Exact proportional relationship.")

# 2. Good correlation (Enrollments vs Revenue)
good_corr = df_yearly["enrollments"].corr(df_yearly["revenue"])
relation_type_good = "Positive" if good_corr > 0 else "Negative"
print(f"[Good Correlation] Enrollments vs Revenue → Coefficient = {good_corr:.2f} ({relation_type_good})")

# 3. Weak/Bad correlation (Ratings vs Enrollments)
bad_corr = df_yearly["rating"].corr(df_yearly["enrollments"])
relation_type_bad = "Positive" if bad_corr > 0 else "Negative"
print(f"[Weak/Bad Correlation] Ratings vs Enrollments → Coefficient = {bad_corr:.2f} ({relation_type_bad})")

plt.show()

