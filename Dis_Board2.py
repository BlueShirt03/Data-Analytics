import pandas as pd
import seaborn as sns
from plotnine import ggplot, aes, geom_point, labs, theme_minimal, theme, element_text
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Hours_Studied": [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6],
    "Exam_Score":    [58, 62, 65, 67, 70, 74, 78, 81, 85, 89],
    "Group": ["No Tutoring", "No Tutoring", "No Tutoring", "No Tutoring", "Tutoring",
              "Tutoring", "Tutoring", "Tutoring", "Tutoring", "Tutoring"]
})


# Original version with Matplotlib
plt.figure(figsize=(7, 5))
for group, subset in df.groupby("Group"):
    plt.scatter(subset["Hours_Studied"], subset["Exam_Score"], label=group, s=70)

plt.title("Study Time vs Exam Score (Matplotlib)")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.legend()
plt.tight_layout()
plt.show()

# Original version with Seaborn
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="Hours_Studied", y="Exam_Score", hue="Group", s=90)

plt.title("Study Time vs Exam Score (Seaborn)")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.tight_layout()
plt.show()

# Improved version with Matplotlib
plt.figure(figsize=(7, 5))
for group, subset in df.groupby("Group"):
    plt.scatter(subset["Hours_Studied"], subset["Exam_Score"], label=group, s=90, alpha=0.9)

plt.title("Study Time vs Exam Score (Matplotlib)", fontsize=14)
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.grid(True, alpha=0.25)
plt.legend(title="Group", frameon=False)

ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()


#Improved version with Seaborn
sns.set_theme(style="whitegrid")

plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="Hours_Studied", y="Exam_Score", hue="Group", s=95, alpha=0.9)

plt.title("Study Time vs Exam Score (Seaborn)", fontsize=14)
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
sns.despine()
plt.tight_layout()
plt.show()


p = (
    ggplot(df, aes(x="Hours_Studied", y="Exam_Score", color="Group"))
    + geom_point(size=3)
    + labs(
        title="Study Time vs Exam Score (plotnine)",
        x="Hours Studied",
        y="Exam Score"
    )
    + theme_minimal()
    + theme(figure_size=(7, 5), plot_title=element_text(size=14))
)

p.show()


