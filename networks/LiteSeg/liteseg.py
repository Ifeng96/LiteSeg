#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 12:00:52 2019

@author: Taha Emara  @email: taha@emaraic.com
"""
import torch 

from networks.LiteSeg import liteseg_shufflenet as shufflenet
from networks.LiteSeg import liteseg_mobilenet as mobilenet

def LiteSeg(num_class, backbone_network, pretrain_weight,is_train=False):

        if backbone_network.lower() == 'shufflenet':
            net = shufflenet.RT(n_classes=num_class, pretrained=is_train, PRETRAINED_WEIGHTS=pretrain_weight)
        elif backbone_network.lower() == 'mobilenet':
            net = mobilenet.RT(n_classes=num_class,pretrained=is_train, PRETRAINED_WEIGHTS=pretrain_weight)
        else:
            raise NotImplementedError
            
        print("Using LiteSeg with", backbone_network)

        return net
        
            
    
