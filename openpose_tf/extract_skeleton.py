import numpy as np


def extract(human):
    """takes a human tf-openpose object and returns parsed skeleton coordinates and probabilities """
    all_points = [x for x in range(18)]
    skeleton = []
    probs = []
    kpts = []
    coords_x= []
    coords_y= []
    subscriptable = str(human).split("BodyPart:")[1:]
    for x in subscriptable:
        kpts.append(int((x.split('-')[0])))
        original_kpts.append(int((x.split('-')[0])))
        coords_x.append(float((str(x.split('-')[1]).split(" score=")[0][1:5]))*image.shape[1])
        coords_y.append(float((str(x.split('-')[1]).split(" score=")[0][6:11]))*image.shape[0])
        probs.append(float(str(x.split('-')[1]).split(" score=")[1]))
    
    for point in range(len(all_points)): # this ensures that undetected kpoints still have a value (nan) 
        if all_points[point] not in kpts:
            kpts.insert(all_points[point], point)
            coords_x.insert(all_points[point], "nan")
            coords_y.insert(all_points[point], "nan")
            probs.insert(all_points[point], 'nan')
    
    for k,cox, coy, prob in zip(kpts, coords_x, coords_y, probs): 
        if type(cox) == str:
            skeleton.append([cox,coy,prob])
        else:
            skeleton.append([round(cox,2),round(coy,2), prob])
    return(np.array(skeleton))