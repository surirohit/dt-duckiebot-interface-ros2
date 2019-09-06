FROM surirohit/crystal-ros-base:arm32v7

RUN pip3 install picamera

ADD picam/vc.tgz /opt/
COPY picam/00-vmcs.conf /etc/ld.so.conf.d
RUN ldconfig

RUN mkdir -p /home/duckiebot-interface/catkin_ws/src
COPY . /home/duckiebot-interface/catkin_ws/src/

WORKDIR /home/duckiebot-interface