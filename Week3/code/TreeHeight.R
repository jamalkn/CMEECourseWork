# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# ARGUMENTS:
# degrees      The angle of elevation in radians
# distance     The distance from base (e.g., meters)
#
# OUTPUT:
# The heights of the tree, same units as "distance"<
MyData <- read.csv(file="../data/trees.csv", header=TRUE, sep=",")

TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  return (height)
}



qw<-TreeHeight(2,3)


Species<-MyData[,1]
Distance.m<-MyData[,2]
Angle.degrees<-MyData[,3]


Tree.Height.m<-double(nrow(MyData))

for (i in 1:nrow(MyData)) {
	Tree.Height.m[i]<- TreeHeight(MyData[i,3],MyData[i,2])
}








#Tree.Height.m<-TreeHeight(MyData[,2]*10,(MyData[,3])
#Tree.Height.m<-MyData[,2]*10*tan(MyData[,3]*pi/180)
new <- data.frame(Species,Distance.m,Angle.degrees,Tree.Height.m)
write.csv(new,"TreeHts.csv")



