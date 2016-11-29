using UnityEngine;
using System.Collections;
using SocketIO;

public class StinkomatController : MonoBehaviour {
	private const int numScents = 6;

	public SocketIOComponent client;
	[Range(0, numScents - 1)]
	public int[] scents;

	// Use this for initialization
	void Start () {

	}

	// Update is called once per frame
	void Update () {

	}

	new void OnTriggerEnter() {
		Debug.Log("Trigger enter");
		foreach (int scent in scents)
			client.Emit("activate", new JSONObject(scent));
	}

	new void OnTriggerExit() {
		Debug.Log("Trigger exit");
		foreach (int scent in scents)
			client.Emit("deactivate", new JSONObject(scent));
	}
}
