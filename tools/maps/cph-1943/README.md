# Copenhagen 1943 map (Annemarie's Path, NTS kit)

The Copenhagen view in `assets/js/oao-nts-kit.js` (`CPH_SVG`) is generated here.

- `osm-data.txt` - shorelines, harbor, canals, moats, lakes and parks pulled from OpenStreetMap (Overpass API, Oct 2026), simplified. Units are 1e-5 degrees offset from 12.5 E / 55.6 N.
- `build.py` - assembles the coastline into land and water with shapely, unions the lakes/canals/moats, writes `paths.json`.
- `gen.py` - lays out roads, labels, cartouche, scale bar and compass and writes `map.svg.txt` (paths in both scripts point at a scratch folder; change them before re-running).
- Frame: 12.530-12.612 E, 55.6685-55.706 N, north up, true scale (1 km = 124 px in the 640-wide viewBox).

1943 checks: the frame stops short of land filled after the war (eastern Refshaleøen and Lynetten, 1950s-1981; Nordhavn). Everything drawn existed in 1943: the lakes, Kastellet and its moats, Christianshavn's ramparts, Holmen, the Free Port basins (1894), Langelinie, Fælledparken (1909), Tivoli (1843).
Pin x/y in `CPH_PINS` use the same projection as the map (`P()` in build.py): x = (lon-12.53)*1e5*0.07805, y = (55.706-lat)*1e5*0.07805*1.7727.
Map data (c) OpenStreetMap contributors, ODbL. The credit is printed on the map.
