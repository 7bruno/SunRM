from http import HTTPStatus

from ..models import Hsp
from ..schema import hsps_schema
from .http_service import build_api_response, build_response_message
from .uf_dict_service import ufs_dict


def get_uf_or_all(**kwargs):
    request_uf = kwargs.get("uf")
    if request_uf and request_uf.isupper():
        return "Not found", HTTPStatus.NOT_FOUND

    try:

        if request_uf:
            uf = ufs_dict[request_uf]
            ufs = Hsp.query.filter_by(uf=uf).all()
            if not len(ufs):
                return build_api_response(HTTPStatus.BAD_REQUEST)

            return build_api_response(HTTPStatus.OK, {
                "data": hsps_schema.dump(ufs)})

        else:
            uf_list = list(ufs_dict.keys())

            return build_api_response(HTTPStatus.OK, {"uf": uf_list})

    except Exception as error:
        print(error)
        return build_api_response(HTTPStatus.INTERNAL_SERVER_ERROR, {
            "info": "Internal server error"
        })
