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

# cv2.destroyAllWindows() # destroy all windows