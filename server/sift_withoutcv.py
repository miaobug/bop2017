#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import mahotas as mh
from mahotas.features import surf
import numpy as np
import os
import sys
max_features = 512

def compute_dist (vec1, vec2):
    dist = np.sqrt(np.sum(np.square(vec1 - vec2)))
    return dist

def compute_similarity (vecs1, vecs2, accept_rate = 0.4):
    if len(vecs1)<2 or len(vecs2)<2:
        return 0
    match_count = 0
    for vec1 in vecs1:
        temp_list = []
        for vec2 in vecs2:
            temp_list.append(compute_dist(vec1,vec2))
        temp_list = sorted(temp_list)
        if temp_list[0]/temp_list[1]<accept_rate:
            match_count +=1
    return match_count

def get_intros(img):
    image = mh.imread(img,as_grey=True)
    query_features = surf.surf(image,max_points=max_features)
    best_match = ''
    similarity = 0.0
    for parent, dirnames, filenames in os.walk('./server/imgs/'):
        for filename in filenames:
            image = mh.imread(os.path.join(parent, filename),as_grey=True)
            sample_features = surf.surf(image,max_points=max_features)
            temp_similarity = compute_similarity(query_features,sample_features)
            if temp_similarity>similarity:
                best_match = filename
                similarity = temp_similarity
    if best_match != '':
        print('best match filename '+best_match)
        f = open('./server/intros/'+best_match.split('.')[0] + '.txt')
        # print f.read()
        return f.read()
    else:
        res = '您的图片未找到'
        print res
        return res

if __name__ == "__main__":
    img = sys.argv[1]
    print get_intros(img)
