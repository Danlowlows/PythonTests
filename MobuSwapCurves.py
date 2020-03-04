from pyfbsdk import FBSystem, FBModel, FBModelSkeleton, FBModelNull, FBModelMarker

def GetSelected():
    return [obj for obj in FBSystem().Scene.Components if obj.Selected and (isinstance(obj, FBModel) or isinstance(obj, FBModelSkeleton) or isinstance(obj, FBModelNull) or isinstance(obj, FBModelMarker))]

def GetCurve(obj, propName, sourceDof):
    return obj.PropertyList.Find(propName).GetAnimationNode().Nodes[sourceDof].FCurve

def SetCurve(obj, propName, targetDof, sourceCurve):
    obj.PropertyList.Find(propName).GetAnimationNode().Nodes[targetDof].FCurve = sourceCurve

def SwapCurves(propName, dof1, dof2):
    selectedList = GetSelected()
    for obj in selectedList:
        curve1 = GetCurve(obj, propName, dof1)
        curve2 = GetCurve(obj, propName, dof2)
        SetCurve(obj, propName, dof1, curve2)
        SetCurve(obj, propName, dof2, curve1)

def SwapTransXY():
    SwapCurves("Lcl Translation", 0, 1)

def SwapTransYZ():
    SwapCurves("Lcl Translation", 1, 2)

def SwapTransXZ():
    SwapCurves("Lcl Translation", 0, 2)

def SwapRotXY():
    SwapCurves("Lcl Rotation", 0, 1)

def SwapRotYZ():
    SwapCurves("Lcl Rotation", 1, 2)

def SwapRotXZ():
    SwapCurves("Lcl Rotation", 0, 2)
