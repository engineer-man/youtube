using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CubeController : MonoBehaviour {

    enum Direction { LEFT, RIGHT };

    public GameObject cube;

    Direction dir = Direction.RIGHT;

    void Update() {
        cube.transform.Rotate(.2f, -.3f, .1f);

        float z = Mathf.Clamp(cube.transform.position.z, -15f, 15f);

        if (z == -15f)
            dir = Direction.RIGHT;
        if (z == 15f)
            dir = Direction.LEFT;

        z += dir == Direction.RIGHT ? .08f : -.08f;

        Vector3 position = new Vector3(
            cube.transform.position.x,
            cube.transform.position.y,
            z
        );

        cube.transform.position = position;
    }

}
