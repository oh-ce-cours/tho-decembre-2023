# https://stackoverflow.com/questions/7008608/scipy-io-loadmat-nested-structures-i-e-dictionaries

import scipy
import numpy as np
import matplotlib.pyplot as plt


def loadmat(filename):
    '''
    this function should be called instead of direct spio.loadmat
    as it cures the problem of not properly recovering python dictionaries
    from mat files. It calls the function check keys to cure all entries
    which are still mat-objects
    '''
    matlab_struct = spio.matlab.mio5_params.mat_struct


    def _check_keys(d):
        '''
        checks if entries in dictionary are mat-objects. If yes
        todict is called to change them to nested dictionaries
        '''
        for key in d:
            if isinstance(d[key], matlab_struct):
                d[key] = _todict(d[key])
        return d

    def _todict(matobj):
        '''
        A recursive function which constructs from matobjects nested dictionaries
        '''
        d = {}
        for strg in matobj._fieldnames:
            elem = matobj.__dict__[strg]
            if isinstance(elem, matlab_struct):
                d[strg] = _todict(elem)
            elif isinstance(elem, np.ndarray):
                d[strg] = _tolist(elem)
            else:
                d[strg] = elem
        return d

    def _tolist(ndarray):
        '''
        A recursive function which constructs lists from cellarrays
        (which are loaded as numpy ndarrays), recursing into the elements
        if they contain matobjects.
        '''
        elem_list = []
        for sub_elem in ndarray:
            if isinstance(sub_elem, matlab_struct):
                elem_list.append(_todict(sub_elem))
            elif isinstance(sub_elem, np.ndarray):
                elem_list.append(_tolist(sub_elem))
            else:
                elem_list.append(sub_elem)
        return elem_list

    data = scipy.io.loadmat(filename, struct_as_record=False, squeeze_me=True)
    return _check_keys(data)


if __name__ == "__main__":

    d = loadmat("./exemple1.mat")
    function_record = d["FRF"]["function_record"]
    x_values = d["FRF"]["x_values"]
    x_values["start_value"]
    x_values["increment"]
    x_values["number_of_values"]
    y_values = d["FRF"]["y_values"]

    y_values["quantity"]
    # {'info': 'Data saved by Test.Lab in MKS',
    #  'label': '(m/s^2)/N',
    #  'quantity_terms': [{'den': 1, 'num': 0, 'quantity': 'LENGTH'},
    #   {'den': 1, 'num': 0, 'quantity': 'ANGLE'},
    #   {'den': 1, 'num': -1, 'quantity': 'MASS'},
    #   {'den': 1, 'num': 0, 'quantity': 'TIME'},
    #   {'den': 1, 'num': 0, 'quantity': 'CURRENT'},
    #   {'den': 1, 'num': 0, 'quantity': 'LIGHT'},
    #   {'den': 1, 'num': 0, 'quantity': 'TEMPERATURE'},
    #   {'den': 1, 'num': 0, 'quantity': 'MOLCULAR_AMOUNT'}],
    #  'unit_transformation': {'factor': 1, 'log_reference': 1, 'offset': 0}}

    y_val = np.array(y_values["values"])
    # array([[-1.87352262e-02+0.00000000e+00j,  7.48587865e-03+0.00000000e+00j,
    #         -7.39470050e-02+0.00000000e+00j, ...,
    #         -2.55687386e-01+0.00000000e+00j, -2.05759358e+00+0.00000000e+00j,
    #         -5.40898860e-01+0.00000000e+00j],
    #        [ 2.82911211e-03+1.05455341e-02j,  1.18594419e-03+7.01557705e-03j,
    #         -3.58894654e-03+1.40859559e-02j, ...,
    #          1.18086832e-02+1.15464263e-01j, -6.78310394e-02+3.98983777e-01j,
    #         -2.16271579e-02+1.66353047e-01j],
    #        [ 8.87264125e-03+1.99012388e-03j,  5.81436651e-03-2.61044683e-04j,
    #          6.01190235e-03+4.58421977e-03j, ...,
    #          4.76684570e-02+5.20035066e-02j,  7.26426244e-02+2.12621331e-01j,
    #          3.07634138e-02+8.56350362e-02j],
    #        ...,
    #        [-1.23164201e+00-3.05321310e-02j, -2.99964595e+00-6.55095726e-02j,
    #          1.88302553e+00+5.76530881e-02j, ...,
    #          1.44582701e+00+7.65593499e-02j, -6.61198950e+00-3.15508731e-02j,
    #          6.16515779e+00-6.87230304e-02j],
    #        [-1.28100801e+00+1.73686296e-02j, -3.08021355e+00-1.47453532e-01j,
    #          1.88631976e+00+6.55868798e-02j, ...,
    #          1.44679165e+00+3.84851210e-02j, -7.17346525e+00-7.45063275e-02j,
    #          6.27492285e+00-3.15349042e-01j],
    #        [-1.13666809e+00+0.00000000e+00j, -3.22147202e+00+0.00000000e+00j,
    #          1.90531623e+00+0.00000000e+00j, ...,
    #          1.37329578e+00+0.00000000e+00j, -7.44830799e+00+0.00000000e+00j,
    #          6.32863617e+00+0.00000000e+00j]])

    # np.array(y_values["values"]).shape
    # (2049, 234)

    plt.plot(np.absolute(y_v[0]))
    plt.show()
