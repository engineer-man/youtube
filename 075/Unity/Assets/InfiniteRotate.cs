using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class InfiniteRotate : MonoBehaviour {

    // Update is called once per frame
    void Update() {
        transform.Rotate(.2f, -.3f, .1f);
    }

}
