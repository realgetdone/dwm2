install.packages(c("arules", "arulesViz"), dependencies = FALSE)

# Install required packages (run only once)
install.packages("arules")
install.packages("arulesViz")
# Load libraries
library(arules)
library(arulesViz)
# -----------------------------
# 1. Create a small transaction dataset
# -----------------------------
# Each line is a "basket" of items
groceries <- list(
  c("milk", "bread", "eggs"),
  c("milk", "bread"),
  c("milk", "soda", "beer"),
  c("bread", "butter"),
  c("milk", "bread", "soda", "beer"),
  c("bread", "butter", "jam")
)
# Convert list into transactions
trans <- as(groceries, "transactions")
inspect(trans[1:5])
# Step 1: Rename in the list before transactions


groceries <- lapply(groceries, function(x) gsub("soda", "soft_drink", x))
# Step 2: Convert to transactions
trans_clean <- as(groceries, "transactions")
# Step 3: Filter sparse items (>= 2 occurrences)
trans_up <- trans_clean[, itemFrequency(trans_clean) >= (2/length(trans_clean)
# Step 4: Inspect
cat("Dimensions after cleaning:\n")
print(dim(trans_up))
inspect(trans_up)
# Step 5: Item frequencies
itemFrequency(trans_up)
rules <- apriori(
  trans_up,
  parameter = list(supp = 0.2, conf = 0.6, minlen = 2)


itemFrequencyPlot(trans_up, topN = 5, col = "skyblue",
                  main = "Top 5 Items", type = "absolute")



plot(rules, method = "grouped matrix", measure = "lift")