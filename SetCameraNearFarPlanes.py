from pyfbsdk import FBSystem, FBApplication

def SetCameraFarPlane():
    for camera in FBSystem().Scene.Cameras:
        camera.NearPlaneDistance = 10.0
        camera.FarPlaneDistance = 1000000.0

def CameraFarPlaneCallback(pCaller, pEvent):
    SetCameraFarPlane()

def SetCameraFarPlaneCallback():
    app = FBApplication()
    app.OnFileNewCompleted.Add(CameraFarPlaneCallback)
    app.OnFileOpenCompleted.Add(CameraFarPlaneCallback)

SetCameraFarPlaneCallback()