import cv2
import mediapipe
import pygame
import random
import conf
from conf import *

pygame.init()

video = cv2.VideoCapture(0)
screen = pygame.display.set_mode((620,600))
pygame.display.set_caption("WebCamera")
clock = pygame.time.Clock()
mp_drawing = mediapipe.solutions.drawing_utils
mp_face_mesh = mediapipe.solutions.face_mesh
detector = mp_face_mesh.FaceMesh(max_num_faces=1,refine_landmarks=True,min_detection_confidence=0.5,min_tracking_confidence=0.5)
hand_detector = mediapipe.solutions.hands.Hands(max_num_hands=1,min_detection_confidence=0.5,min_tracking_confidence=0.5)

# pic = pygame.image.load("anonym.jpg")
# pic = pygame.transform.scale(pic,(720,700))
# img = cv2.imread("C:\\Users\\windows X\\Downloads/Telegram Desktop/5013_Foto/Foto/foto-master/images/porfolio-16-300x500.jpg")
run = True
while run:
	# screen.blit(pic,(0,0))
	screen.fill((20,20,20))
	frame,img = video.read()
	resoult = detector.process(img)
	hand = hand_detector.process(img)
	if hand.multi_hand_landmarks:
		conf.DrawHands(screen,hand)
	
	if resoult.multi_face_landmarks:
		conf.DrawAvatar(screen,resoult)

	# cv2.imshow("face",img)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# pygame.surfarray.blit_array(screen,img)
	pygame.display.update()
	clock.tick(999)
	print(clock.get_fps())
video.release()
cv2.destroyAllWindows()
