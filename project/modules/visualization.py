import sys # to access the system
import cv2

def plot_by_genre():
    print('opening window..')
    img = cv2.imread("resources/figures/plot_by_genre.png", cv2.IMREAD_ANYCOLOR)
    # img = cv2.imread("project/resources/figures/plot_by_genre.png", cv2.IMREAD_ANYCOLOR)
    cv2.imshow("Plot by genre", img)
    cv2.waitKey(0)

def plot_by_country():
    print('opening window..')
    img = cv2.imread("resources/figures/plot_by_country.png", cv2.IMREAD_ANYCOLOR)
    # img = cv2.imread("project/resources/figures/plot_by_country.png", cv2.IMREAD_ANYCOLOR)

    cv2.imshow("Plot by country", img)
    cv2.waitKey()

def plot_by_most_votes():
    print('function: plot_by_most_votes ')

def show_data():
    print('function: show_data')

def order_by_revenue():
    print('function: order_by_revenue')

def production_countries():
    print('function: production_countries')

def budget_compared_to_revenue():
    print('function: budget_compared_to_revenue')

# cv2.destroyAllWindows() # destroy all windows